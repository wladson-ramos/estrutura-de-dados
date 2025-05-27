# Problema valendo 2 pontos
# Implemente as funcionalidades faltantes da fila encadeada.
# Complete o código abaixo onde é pedido
from typing import List

class No:
    def __init__(self, elemento: int, proximo=None):
        self.elemento = elemento
        self.proximo = proximo

class Fila:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

# Retorna o elemento no início da fila
# Se a fila estiver vazia, retorna None
# Complexidade esperada: O(1)
def acessar(fila: Fila):
    if fila.cabeca is not None:
        return fila.cabeca.elemento
    return None


# Retorna se a fila está vazia
# Complexidade esperada: O(1)
def vazia(fila: Fila) -> bool:
    return fila.cabeca is None


# Insere o elemento no topo da fila
# Retorna True se o elemento foi inserido, False caso contrário
# Complexidade esperada: O(1)
def inserir(fila: Fila, elemento) -> bool:
    novo_no = No(elemento)
    if fila.cauda is None:
        fila.cabeca = novo_no
        fila.cauda = novo_no
    else:
        fila.cauda.proximo = novo_no
        fila.cauda = novo_no
    return True


# Remove o elemento do topo da fila
# Retorna True se o elemento foi removido, False caso contrário
# Complexidade esperada: O(1)
def remover(fila: Fila) -> bool:
    if fila.cabeca is None:
        return False
    if fila.cabeca == fila.cauda:
        fila.cabeca = None
        fila.cauda = None
        return True

    fila.cabeca = fila.cabeca.proximo
    return True


# Exibe os elementos da fila
# Complexidade: O(n)
def imprimir(fila: Fila) -> None:
    print("Inicio: ", end="")
    atual = fila.cabeca
    while atual != None:
        if atual.proximo == None:
            print(atual.elemento, end="")
        else:
            print(atual.elemento, end=" -> ")
        atual = atual.proximo
    print(" final")


# Testando a fila #
fila = Fila()
inserir(fila, 10)
inserir(fila, 20)
inserir(fila, 30)
inserir(fila, 40)
imprimir(fila)
print("Fila esperada: 10, 20, 30, 40")
remover(fila)
remover(fila)
inserir(fila, 50)
inserir(fila, 60)
print("Fila esperada: 30, 40, 50, 60")
imprimir(fila)

