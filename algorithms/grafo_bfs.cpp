#include <iostream>
#include <list>
using namespace std;

class grafo {
  int n_vertices;
  list<int>* p_a; 
  bool* visitado;

  public:
    grafo(int vertices);
    void agregar_arista(int dato, int siguiente);
    void BFS(int vertice_inicio);
};

grafo::grafo(int vertices) {
  n_vertices = vertices;
  p_a = new list<int>[vertices];
}

//añadir aristas (dato->dato(apuntado))

void grafo::agregar_arista(int dato, int siguiente) {
  p_a[dato].push_back(siguiente);
  p_a[siguiente].push_back(dato);
}

//Busqueda por Anchura (BFS)

void grafo::BFS(int vertice_inicio) {
  visitado = new bool[n_vertices];

  for (int i = 0; i < n_vertices; i++){
    visitado[i] = false;
  }

  list<int> cola;

  visitado[vertice_inicio] = true;
  cola.push_back(vertice_inicio);

  list<int>::iterator i;

  while (!cola.empty()) {
    int vertice = cola.front();
    cout << "vertice visitado -> " << vertice << endl;
    cola.pop_front();
    //vv = vertice visitado
    for (i = p_a[vertice].begin(); i != p_a[vertice].end(); ++i) {
      int vv = *i;
      if (!visitado[vv]) {
        visitado[vv] = true;
        cola.push_back(vv);
      }
    }
  }
}

int main() {

  grafo g(9);
  g.agregar_arista(0,1);
  g.agregar_arista(0,8);
  g.agregar_arista(0,5);
  g.agregar_arista(1,4);
  g.agregar_arista(1,2);
  g.agregar_arista(2,3);
  g.agregar_arista(2,4);
  g.agregar_arista(3,7);
  g.agregar_arista(3,6);
  g.agregar_arista(4,6);
  g.agregar_arista(5,6);

  g.BFS(3);

  return 0;
}
