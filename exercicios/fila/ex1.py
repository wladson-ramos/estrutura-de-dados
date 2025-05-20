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
    return fila.cabeca == None


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
    fila.cabeca = fila.cabeca.proximo
    if fila.cabeca is None:
        fila.cauda = None
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


f = Fila()
print(vazia(f))        # True
inserir(f, 10)
inserir(f, 20)
inserir(f, 30)
imprimir(f)            # Inicio: 10 -> 20 -> 30 final
print(acessar(f))      # 10
remover(f)
imprimir(f)            # Inicio: 20 -> 30 final
