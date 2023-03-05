#include <clocale>
#include <iostream>

int main(int argc, char const *argv[])
{
    /*вывод ПРИВЕТ с установкой функции кодировки русского 
    языка*/
    setlocale(LC_ALL, "Rus");
    std::cout << "привет!" << std::endl;
    return 0;
}
