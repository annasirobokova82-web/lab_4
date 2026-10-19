number = int(input("Введите число: "))

if number % 2 == 0:
    print(f"Число {number} – чётное")
else:
    print(f"Число {number} – нечётное")

if number % 3 == 0:
    print(f"Число {number} делится на 3")
else:
    print(f"Число {number} не делится на 3")

if number > 0:
    print("Число положительное")
elif number < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")