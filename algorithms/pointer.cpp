#include <iostream>
using namespace std;
int main(){

    string food = "Pizza"; // A food variable of type string
    string* ptr = &food;    // A pointer to food

    cout << food << "\n";   // Outputs Pizza
    cout << &food << "\n";  // Outputs the memory address of food
    cout << ptr << "\n";   // Outputs the memory address of food

    *ptr = "Hamburger";     // Changes the value of the pointer
    cout << food << "\n";   // Outputs Hamburger
    


    return 0;
}