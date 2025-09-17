import cv2 as cv

def task2():
    # Чтение изображений различных форматов и с различными флагами
    image1 = cv.imread("media/chicken.png", cv.IMREAD_GRAYSCALE)
    image2 = cv.imread("media/chicken.jpg", cv.IMREAD_COLOR_RGB)
    image3 = cv.imread("media/chicken.jpeg", cv.IMREAD_REDUCED_COLOR_8)

    # Создание окон с различными флагами
    cv.namedWindow("Chicken gray", cv.WINDOW_AUTOSIZE)
    cv.namedWindow("Chicken RGB", cv.WINDOW_KEEPRATIO)
    cv.namedWindow("Chicken reduced", cv.WINDOW_FREERATIO)

    # Отображение изображений в окнах
    cv.imshow("Chicken gray", image1)
    cv.imshow("Chicken RGB", image2)         
    cv.imshow("Chicken reduced", image3)
    
    cv.waitKey(0)
    cv.destroyAllWindows()

# Функция для отображения видео по пути path в окне с именем name и опциями options
def show_video(path, name, *options):
    cap = cv.VideoCapture(path)
    cv.namedWindow(name, cv.WINDOW_NORMAL)
    if "resize" in options:
        cv.resizeWindow(name, 1080, 360)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if "gray" in options:
            frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        if "colormap" in options:
            frame = cv.applyColorMap(frame, cv.COLORMAP_JET)
        cv.imshow(name, frame)
        if cv.waitKey(25) & 0xFF == 27:
            break
    cap.set(cv.CAP_PROP_POS_FRAMES, 0)
    cv.destroyWindow(name)

# Вывод видео в различных форматах
def task3():
    show_video("media/guy.mp4", "Original video")
    show_video("media/guy.mp4", "Resized video", "resize")
    show_video("media/guy.mp4", "Gray video", "gray")
    show_video("media/guy.mp4", "Colormapped video", "colormap")

# Считывание видео из файла и запись его в другой файл
def task4():
    input_path = "media/guy.mp4"
    output_path = "media/output.mp4"

    cap = cv.VideoCapture(input_path)

    fps = cap.get(cv.CAP_PROP_FPS)
    w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    out = cv.VideoWriter(output_path, fourcc, fps, (w, h))

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)

    cap.release()
    out.release()
    cv.destroyAllWindows()


def task5():
    img = cv.imread("media/chicken.png")
    img_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    cv.namedWindow("Chicken BGR", cv.WINDOW_AUTOSIZE)
    cv.namedWindow("Chicken HSV", cv.WINDOW_AUTOSIZE)

    cv.imshow("Chicken BGR", img)
    cv.imshow("Chicken HSV", img_HSV)

    cv.waitKey(0)
    cv.destroyAllWindows()

task5()
