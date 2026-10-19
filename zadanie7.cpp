#include <iostream>

int main() {
    double a, b, c;
    std::cout << "Введите стороны a, b, c: ";
    std::cin >> a >> b >> c;

    if (a + b > c && a + c > b && b + c > a) {
        if (a == b && b == c) std::cout << "Равносторонний\n";
        else if (a == b || a == c || b == c) std::cout << "Равнобедренный\n";
        else std::cout << "Разносторонний\n";
    } else {
        std::cout << "Треугольник не существует\n";
    }
    return 0;
}