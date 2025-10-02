import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

# Пункт 1.
# Параметры ядра свёртки
KERNEL_SIZE = 5
BLUR_PARAMETER = 5

# Построение ядра свёртки по формуле матрицы Гаусса
def get_kernel(kernel_size, blur_parameter):
    ker = np.zeros((kernel_size, kernel_size), dtype=float)
    a = kernel_size - kernel_size // 2
    b = a
    for i in range(kernel_size):
        for j in range(kernel_size):
            x, y = i+1, j+1
            val = (1 / (2* np.pi * blur_parameter**2)) * np.exp(-(((x-a)**2 + (y-b)**2)/(2 * blur_parameter**2)))
            ker[i, j] = val
    
    return ker

kernel3 = get_kernel(3, BLUR_PARAMETER)
kernel5 = get_kernel(5, BLUR_PARAMETER)
kernel7 = get_kernel(7, BLUR_PARAMETER)
# print(f"РАЗМЕР 3x3:\n{kernel3}")
# print(f"РАЗМЕР 5x5:\n{kernel5}")
# print(f"РАЗМЕР 7x7:\n{kernel7}")

# Пункт 2.
# Нормирование матрицы (сумма элементов должна бстремиться к 1)
kernel3 = kernel3 / kernel3.sum()
kernel5 = kernel5 / kernel5.sum()
kernel7 = kernel7 / kernel7.sum()

# print(f"Нормированная матрица размера 3x3:\n{kernel3}\nСумма элементов: {kernel3.sum()}")
# print(f"Нормированная матрица размера 5x5:\n{kernel5}\nСумма элементов: {kernel5.sum()}")
# print(f"Нормированная матрица размера 7x7:\n{kernel7}\nСумма элементов: {kernel7.sum()}")

# Пункт 3.
while True:
    ret, frame = cap.read()
    if not ret:
        break

    grayscale_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("Video", grayscale_frame)

    key = cv.waitKey(1)
    if key & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()