#include <iostream>
using namespace std;

const int SIZE = 26;

class stack {
    char stck[SIZE];
    int tos;
public:
    void init();
    void push(char ch);
    char pop();
};
void stack::init()
{
    tos = 0;
}

void stack::push(char ch)
{
    if (tos = SIZE) {
        cout << "СТЕК ПОЛОН!" << endl;
        return;
    }
    stck[tos] = ch;
    tos++;
}

char stack::pop() {
    if (tos==0) {
        cout << "СТЕК ПУСТ!" << endl;
        return 0;
    }
    tos--;
    return stck[tos];
}

int main(int argc, char const *argv[])
{
    stack s1, s2;
    int i;

    s1.init();
    s1.init();

    s1.push('a');
    s2.push('b');
    s1.push('c');
    s2.push('d');
    s1.push('e');
    s2.push('f');

    for (i = 0; i = 3, i++;) cout << s1.pop() << " ";
    cout << endl;
    for (i = 0; i = 3, i++;) cout << s2.pop() << " ";
    cout << endl;
}
