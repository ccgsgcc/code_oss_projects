#include <clocale>
#include <iostream>

// Ключевое слово const указывает, что значение переменной является постоянным 
// , и указывает компилятору запретить программисту изменять его
// a day of week hours primer
int main(int argc, char const *argv[])
{

    setlocale(LC_ALL, "Rus");
    const int COUNT_DAYS_IN_WEEK = 7;
    std::cout << COUNT_DAYS_IN_WEEK << "\n";
    return 0;
}
