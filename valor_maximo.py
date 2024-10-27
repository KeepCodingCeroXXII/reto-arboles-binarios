lista_anidada = [
  1,
  [7,
    [2, [], []],
    [6, 
      [5, [], []],
      [11, [], []]]],
  [9,
    [],
    [9, 
      [5, [], []],
      []]]
]        

def crear_lista_extendida(lista_anidada):
    """
    A partir de una lista anidada (representación de un árbol), se extrae 
    todos los elementos, de las listas conformadas por los todos los nodos, en una lista no anidada(lista extendida.)
    """
    lista_extendida = []


    elem_extraer = [lista_anidada]

    while elem_extraer : 
        # se Extra el primer elemento de la lista anidada         #        
        elemento = elem_extraer.pop(0)
        
        if isinstance(elemento, list):
            # Si el elemento es una lista, esto es,si encontramos una lista dentro de elem_extraer, 
            # se extrae  todos sus subelementos y evaluamos subelemnto por subelemento en los siguientes recorridos. hastanque no existan sublistas         
            elem_extraer = elemento + elem_extraer 
            
        else:
            # Si no es una lista, lo agreañadimos a la lista extendida
              lista_extendida.append(elemento)


    return  lista_extendida 


lista_extendida =  crear_lista_extendida(lista_anidada )

print(f'Lista extendida: {lista_extendida}')
print(f'Valor máximo: {max(lista_extendida)}')


     
