#include <iostream>
#include <list>
using namespace std;

class grafo{
    int V; 
    list<int> *adj;
    bool *visitado;
public:
        grafo(int V); 
        void agregarArista(int v,int w); 
        void DFS(int v);
};
grafo::grafo(int V){
    this->V = V;
    adj = new list<int>[V];
    this->visitado = new bool[this->V];
    for(int i=0;i<this->V;i++) {
        this->visitado[i] = false;
    }
}
void grafo::agregarArista(int v,int w){
    adj[v].push_back(w);
}
void grafo::DFS(int v){
    //nodo actual (visitado)
    this->visitado[v] = true; 
    cout << v << " ";

    list<int>::iterator p;
    for(p = adj[v].begin(); p!=adj[v].end();++p){ 
        if(!this->visitado[*p]){
            DFS(*p);
        }
    }
}
int main(){
    int V = 4;
    grafo g(V);
    g.agregarArista(0,1);
    g.agregarArista(0,2);
    g.agregarArista(1,2);
    g.agregarArista(2,0);
    g.agregarArista(2,3);
    g.agregarArista(3,3);

    int x = 2;

    cout << "DFS " << x <<" : "<<endl ;
    
    g.DFS(x);
    
    return 0;
}