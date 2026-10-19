import math

print("Проверка попадания точки в круг (центр в 0,0)")
x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))
r = float(input("Введите радиус круга R: "))

# Квадрат расстояния от точки до центра (0,0)
distance_sq = x**2 + y**2
radius_sq = r**2

if r <= 0:
    print("Ошибка: радиус должен быть положительным!")
elif distance_sq < radius_sq:
    print(f"Точка ({x}, {y}) находится ВНУТРИ круга.")
elif distance_sq == radius_sq:
    print(f"Точка ({x}, {y}) находится НА ГРАНИЦЕ круга.")
else:
    print(f"Точка ({x}, {y}) находится СНАРУЖИ круга.")