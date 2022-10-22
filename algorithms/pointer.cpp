#include <iostream>
using namespace std;
int main(){

    string food = "Pizza"; // A food variable of type string
    string &meal = food;    // A reference to food

    cout << food << "\n";   // Outputs Pizza
    cout << meal << "\n";   // Outputs Pizza
    


    return 0;
}