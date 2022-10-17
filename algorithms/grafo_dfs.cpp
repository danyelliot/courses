#include <bits/stdc++.h>
using namespace std;

class grafo {
public:
	map<int, bool> visitado;
	map<int, list<int> > lista_adyacencia;

	
	void agregar_arista(int vertice, int siguiente);
	void DFS(int vertice);
};

void grafo::agregar_arista(int vertice, int siguiente)
{
	lista_adyacencia[vertice].push_back(siguiente); 
}

void grafo::DFS(int vertice)
{
	
	visitado[vertice] = true;
	cout << "vertice -> "<<vertice << "\n";

	list<int>::iterator i;
	for (i = lista_adyacencia[vertice].begin(); i != lista_adyacencia[vertice].end(); ++i){
		if (!visitado[*i]){
			DFS(*i);
		}
	}

}

int main()
{
	
	grafo g ; 
    g.agregar_arista(0,1);
    g.agregar_arista(0, 2);
    g.agregar_arista(1, 2);
    g.agregar_arista(2, 0);
    g.agregar_arista(2, 3);
    
    int i ;
	cout << "Ingrese vertice de inicio: " ;cin >> i ;
	cout << "\nAlgoritmo DFS\n"<<endl;
	g.DFS(i);

	return 0;
}

