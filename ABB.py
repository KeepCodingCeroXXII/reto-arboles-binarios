class Nodo:

    """
    La clase Nodo tiene un  valor y referencias a los hijos izquierdo y derecho. Tiene un metódo insertar para
    insertar valores dependiendo del valor del nodo y un metodo de buqueda que encuentra el valor y los nodos recorridos

    
    """
    def __init__(self, valor):
        self.valor = valor 
        self.izquierda = None 
        self.derecha = None   
        self.coste_ultima_busqueda = 0
  
    
    def buscar(self, valor):    
        self.coste_ultima_busqueda += 1
    
        if valor == self.valor:
              return self.valor 
          
        elif valor < self.valor and self.izquierda :
              return self.izquierda.buscar(valor)
          
        elif valor > self.valor and self.derecha:
              return self.derecha.buscar(valor)
          
        return None        
        
    
    def insertar(self, valor):
        if valor < self.valor:
            if self.izquierda is None:
                self.izquierda = Nodo(valor)
            else:
                self.izquierda.insertar(valor)
        else:
            if self.derecha is None:
                self.derecha = Nodo(valor)
            else:
                self.derecha.insertar(valor)   

    
    def __repr__(self):
        return f"Nodo({self.valor})"
    
numeros = [66, 34, 79, 26, 83, 39, 32, 60, 22, 74, 37, 80, 82, 50, 73, 66, 31, 44, 33, 51]


# Inserta los números en el árbol
arbol = Nodo(numeros[0])
for num in numeros[1:]:
    arbol.insertar(num)


# Búsca un valor
nodo_buscado = arbol.buscar(32)
if nodo_buscado:
    print(f"Nodo encontrado: {nodo_buscado}, coste de búsqueda: {arbol.coste_ultima_busqueda}")
else:
    print("Nodo no encontrado")

# Búsqueda de un valor no existente
nodo_buscado = arbol.buscar(100)

if nodo_buscado:
    print(f"Nodo encontrado: {nodo_buscado}, coste de búsqueda: {arbol.coste_ultima_busqueda}")
else:
    print(f"Nodo no encontrado, coste de búsqueda: {arbol.coste_ultima_busqueda}")