class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, valor)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecho, valor)

    def inorder(self):
        self._inorder_recursivo(self.raiz)

    def _inorder_recursivo(self, nodo):
        if nodo is not None:
            self._inorder_recursivo(nodo.izquierdo)
            print(nodo.valor, end=' ')
            self._inorder_recursivo(nodo.derecho)

    def preorder(self):
        self._preorder_recursivo(self.raiz)

    def _preorder_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.valor, end=' ')
            self._preorder_recursivo(nodo.izquierdo)
            self._preorder_recursivo(nodo.derecho)

    def postorder(self):
        self._postorder_recursivo(self.raiz)

    def _postorder_recursivo(self, nodo):
        if nodo is not None:
            self._postorder_recursivo(nodo.izquierdo)
            self._postorder_recursivo(nodo.derecho)
            print(nodo.valor, end=' ')

# Ejemplo de uso del árbol
arbol = ArbolBinario()
valores = [7, 3, 9, 1, 4, 8, 10]
for val in valores:
    arbol.insertar(val)

print("Recorrido Inorder:")
arbol.inorder()
print("\nRecorrido Preorder:")
arbol.preorder()
print("\nRecorrido Postorder:")
arbol.postorder()
