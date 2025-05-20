from typing import List

class No:
    def __init__(self, elemento: int, proximo):
        self.elemento = elemento
        self.proximo = proximo

class Pilha:
    def __init__(self):
        self.cabeca = None


# Retorna o elemento no topo da pilha
# Se a pilha estiver vazia, retorna None
# Complexidade esperada: O(1)
def acessar(pilha: Pilha):
    if pilha.cabeca is None:
        return None
    return pilha.cabeca.elemento


# Retorna se a pilha está vazia
# Complexidade esperada: O(1)
def vazia(pilha: Pilha) -> bool:
    return pilha.cabeca is None


# Insere o elemento no topo da pilha
# Retorna True se o elemento foi inserido, False caso contrário
# Complexidade esperada: O(1)
def inserir(pilha: Pilha, elemento) -> bool:
    novo_no = No(elemento, pilha.cabeca)
    pilha.cabeca = novo_no
    return True


# Remove o elemento do topo da pilha
# Retorna True se o elemento foi removido, False caso contrário
# Complexidade esperada: O(1)
def remover(pilha: Pilha) -> bool:
    if pilha.cabeca is None:
        return False
    pilha.cabeca = pilha.cabeca.proximo
    return True


# Exibe os elementos da pilha
# Complexidade: O(n)
def imprimir(pilha: Pilha) -> None:
    print("Topo: ", end="")
    atual = pilha.cabeca
    while atual != None:
        if atual.proximo == None:
            print(atual.elemento, end="")
        else:
            print(atual.elemento, end=" -> ")
        atual = atual.proximo
    print(" base")


p = Pilha()
inserir(p, 10)
inserir(p, 20)
inserir(p, 30)
imprimir(p)  # Saída: Topo: 30 -> 20 -> 10 base
print("Topo:", acessar(p))  # Saída: Topo: 30
remover(p)
imprimir(p)  # Saída: Topo: 20 -> 10 base
print("Vazia?", vazia(p))  # Saída: Vazia? False

