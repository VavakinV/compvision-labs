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

# Отображение изображение в форматах BGR и HSV
def task5():
    img = cv.imread("media/chicken.png")
    img_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    cv.namedWindow("Chicken BGR", cv.WINDOW_AUTOSIZE)
    cv.namedWindow("Chicken HSV", cv.WINDOW_AUTOSIZE)

    cv.imshow("Chicken BGR", img)
    cv.imshow("Chicken HSV", img_HSV)

    cv.waitKey(0)
    cv.destroyAllWindows()

# Вывод в окно изображения с камеры с красным крестом в середине
def task6():
    cap = cv.VideoCapture(0)
    cv.namedWindow("Webcam", cv.WINDOW_AUTOSIZE)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        h, w = frame.shape[:2]
        cx, cy = w // 2, h // 2

        rect_w, rect_h = 100, 20
        rect_v_w, rect_v_h = 20, 100

        cv.rectangle(frame, (cx - rect_w // 2, cy - rect_h // 2),
                            (cx + rect_w // 2, cy + rect_h // 2),
                            (0, 0, 255), 2)
        cv.rectangle(frame, (cx - rect_v_w // 2, cy - rect_v_h // 2),
                            (cx + rect_v_w // 2, cy + rect_v_h // 2),
                            (0, 0, 255), 2)

        cv.imshow("Webcam", frame)

        if cv.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv.destroyAllWindows()

# Запись видео с камеры в файл media/web_output.mp4
def task7():
    cap = cv.VideoCapture(0)
    cv.namedWindow("Webcam", cv.WINDOW_AUTOSIZE)

    fps = cap.get(cv.CAP_PROP_FPS)
    w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    out = cv.VideoWriter("media/web_output.mp4", fourcc, fps, (w, h))

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        cv.imshow("Webcam", frame)
        out.write(frame)

        if cv.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    out.release()
    cv.destroyAllWindows()

# Определение цвета центрального пикселя и рисование соответствующего креста
def task8():
    cap = cv.VideoCapture(0)
    cv.namedWindow("Webcam", cv.WINDOW_AUTOSIZE)

    while True:
        ret, frame = cap.read()
        if not ret:
            break


        h, w = frame.shape[:2]
        cx, cy = w // 2, h // 2

        b, g, r = frame[cy, cx]
        print(frame[cy, cx])
        if r >= g and r >= b:
            color = (0, 0, 255)
        elif g >= r and g >= b:
            color = (0, 255, 0)
        else:
            color = (255, 0, 0)

        rect_w, rect_h = 100, 10
        rect_v_w, rect_v_h = 10, 100

        cv.rectangle(frame, (cx - rect_w // 2, cy - rect_h // 2),
                            (cx + rect_w // 2, cy + rect_h // 2),
                            color, -1)

        cv.rectangle(frame, (cx - rect_v_w // 2, cy - rect_v_h // 2),
                            (cx + rect_v_w // 2, cy + rect_v_h // 2),
                            color, -1)

        cv.imshow("Webcam", frame)

        if cv.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv.destroyAllWindows()

# Отображение видео с камеры телефона (через ivCam)
def task9():
    cap = cv.VideoCapture(1)
    cv.namedWindow("PhoneCam", cv.WINDOW_AUTOSIZE)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv.imshow("PhoneCam", frame)

        if cv.waitKey(1) & 0xFF == 27:
            break

    cap.release()
cv.destroyAllWindows()

task9()