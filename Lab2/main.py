import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (10, 10))

trajectory = []

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

    moments = cv.moments(mask)

    area = moments['m00']
    y_coords, x_coords = np.where(mask > 0)

    if area != 0:
        cx = int(moments['m10'] / area)
        cy = int(moments['m01'] / area)
        cv.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

        x_min, x_max = min(x_coords), max(x_coords)
        y_min, y_max = min(y_coords), max(y_coords)

        cv.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 0, 0), 2)

        trajectory.append([cx, cy])
        if len(trajectory) > 60:
            trajectory = trajectory[1:]

    trajectory_formatted = np.array(trajectory, np.int32)
    cv.polylines(frame, [trajectory_formatted], False, (0, 0, 255), 4)
    cv.imshow("Red Tracker", frame)

    key = cv.waitKey(1)
    if key & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()
