import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv.inRange(hsv_frame, lower_red1, upper_red1)
    mask2 = cv.inRange(hsv_frame, lower_red2, upper_red2)
    mask = mask1 | mask2

    # Открытие: erode -> dilate
    mask = cv.erode(mask, kernel, iterations=1)
    mask = cv.dilate(mask, kernel, iterations=1)
    # Закрытие: dilate -> erode
    mask = cv.dilate(mask, kernel, iterations=1)
    mask = cv.erode(mask, kernel, iterations=1)

    output_frame = frame.copy()

    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if contours:
        largest_contour = max(contours, key=cv.contourArea)
        x, y, w, h = cv.boundingRect(largest_contour)

        cv.rectangle(output_frame, (x, y), (x + w, y + h), (0, 0, 0), 2)

        moments = cv.moments(largest_contour)
        if moments['m00'] != 0:
            cx = int(moments['m10'] / moments['m00'])
            cy = int(moments['m01'] / moments['m00'])
            cv.circle(output_frame, (cx, cy), 5, (0, 255, 0), -1)

        area = int(cv.contourArea(largest_contour))
        cv.putText(output_frame,
                   f"Area: {area} px",
                   (10, 30),
                   cv.FONT_HERSHEY_SIMPLEX,
                   1,
                   (0, 255, 0),
                   2)

    cv.imshow("Red Tracker", output_frame)

    key = cv.waitKey(1)
    if key & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()
