from typing import List

class Pilha:
    def __init__(self):
        self.capacidade = 100
        self.tamanho = 0
        self.elementos = [None] * self.capacidade


# Retorna o elemento no topo da pilha
# Se a pilha estiver vazia, retorna None
# Complexidade esperada: O(1)
def acessar(pilha: Pilha):
    if pilha.tamanho == 0:
        return None
    return pilha.elementos[pilha.tamanho - 1]


# Retorna se a pilha está vazia
# Complexidade esperada: O(1)
def vazia(pilha: Pilha) -> bool:
    return pilha.tamanho == 0


# Insere o elemento no topo da pilha
# Retorna True se o elemento foi inserido, False caso contrário
# Complexidade esperada: O(1)
def inserir(pilha: Pilha, elemento) -> bool:
    if pilha.tamanho >= pilha.capacidade:
        return False  # Pilha cheia
    pilha.elementos[pilha.tamanho] = elemento
    pilha.tamanho += 1
    return True


# Remove o elemento do topo da pilha
# Retorna True se o elemento foi removido, False caso contrário
# Complexidade esperada: O(1)
def remover(pilha: Pilha) -> bool:
    if pilha.tamanho == 0:
        return False  # Pilha vazia
    pilha.tamanho -= 1
    pilha.elementos[pilha.tamanho] = None  # Limpa referência (boa prática)
    return True


# Exibe os elementos da pilha
# Complexidade: O(n)
def imprimir(pilha: Pilha) -> None:
    print("Base:", pilha.elementos[:pilha.tamanho], "<-topo")

    
p = Pilha()
inserir(p, 10)
inserir(p, 20)
inserir(p, 30)
imprimir(p)  # Base: [10, 20, 30] <-topo
print("Topo:", acessar(p))  # Topo: 30
remover(p)
imprimir(p)  # Base: [10, 20] <-topo
print("Vazia?", vazia(p))  # Vazia? False
