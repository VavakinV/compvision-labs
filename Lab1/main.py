import cv2 as cv

image1 = cv.imread("C:/Labs/compvis/chicken.png", cv.IMREAD_GRAYSCALE)
image2 = cv.imread("C:/Labs/compvis/chicken.jpg", cv.IMREAD_COLOR_RGB)
image3 = cv.imread("C:/Labs/compvis/chicken.jpeg", cv.IMREAD_REDUCED_COLOR_8)

cv.namedWindow("Chicken gray", cv.WINDOW_AUTOSIZE)
cv.namedWindow("Chicken RGB", cv.WINDOW_FULLSCREEN)
cv.namedWindow("Chicken reduced", cv.WINDOW_FREERATIO)

cv.imshow("Chicken gray", image1)
cv.imshow("Chicken RGB", image2)         
cv.imshow("Chicken reduced", image3)
 
cv.waitKey(0)
cv.destroyAllWindows()

video = cv.VideoCapture("C:/Labs/compvis/guy.mp4")
while video:
    ret, frame = video.read()
    cv.imshow('frame', frame)   
    if cv.waitKey(1) & 0xFF == 27:
        break
    cv.waitKey(0)

video = cv.VideoCapture("C:/Labs/compvis/guy.mp4")
while video:
    ret, frame = video.read()
    cv.imshow()
