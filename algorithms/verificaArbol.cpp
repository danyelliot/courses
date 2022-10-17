#include<iostream>
#include <list>
using namespace std;

class Grafo{
        int N;  
        list<int> *lista_adyacencia; 
        bool Ciclo_Recorrido(int n, bool temp[], int siguiente);
    public:
        Grafo(int N);  
        void insertarArista(int n, int m);  
        bool BFS();  
};
 
Grafo::Grafo(int N){
    this->N = N;
    lista_adyacencia = new list<int>[N];
}
void Grafo::insertarArista(int n, int m){
    lista_adyacencia[n].push_back(m); 
    lista_adyacencia[m].push_back(n); 
}
bool Grafo::Ciclo_Recorrido(int n, bool temp[], int siguiente){
    temp[n] = true;   
    list<int>::iterator i;
    for (i = lista_adyacencia[n].begin(); i != lista_adyacencia[n].end(); ++i)
    { 
        if (!temp[*i])
        {
           if (Ciclo_Recorrido(*i, temp, n))
              return true;
        }
        else if (*i != siguiente)
           return true;
    }
    return false;
}
bool Grafo::BFS()
{
    bool *temp = new bool[N];
    for (int i = 0; i < N; i++)
        temp[i] = false;
 
    if (Ciclo_Recorrido(0, temp, -1))
             return false;

    for (int i = 0; i < N; i++)
        if (!temp[i])
           return false;
 
    return true;
}
int esArbol(Grafo G) {
	
    if (G.BFS()){
        return 1;
    } 
    else{
        return 0;
    }
}
 

int main()
{

    Grafo grafo1(10);
    
    grafo1.insertarArista(0,1);
    grafo1.insertarArista(0,2);
    grafo1.insertarArista(1,3);
    grafo1.insertarArista(1,4);
    grafo1.insertarArista(2,5);
    grafo1.insertarArista(3,6);
    grafo1.insertarArista(3,7);
    grafo1.insertarArista(3,8);
    grafo1.insertarArista(4,9);
    
    cout<<"Grafo es un árbol : ";
    cout<<esArbol(grafo1)<<endl;

    // Ahora si juntamos una arista que una el vertice 1-2
    // deberia mostrar que no es un arbol
    cout<<"Añadiendo arista \n";
    cout<<"Grafo es un árbol : ";
    grafo1.insertarArista(1,2);
    cout<<esArbol(grafo1)<<endl;
    return 0;
}
