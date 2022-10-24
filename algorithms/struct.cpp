#include <iostream> 
using namespace std;

struct producto{
    int codigo;
    char nombre[30];
    float precio;
}; typedef producto *pproducto;

int main() {

   pproducto p = new producto;
   (*p).codigo = 123;
    p -> precio  = 12.5;
    p -> precio = 13 ; 
    cout << p -> codigo << endl;
    cout << p -> precio << endl;
    pproducto q = new producto;
    q -> codigo = 456;
    q -> precio = 15.5;
    cout << q -> codigo << endl;
    cout << q -> precio << endl;
    q -> codigo = p -> codigo;
    cout << q -> codigo << endl;
}
