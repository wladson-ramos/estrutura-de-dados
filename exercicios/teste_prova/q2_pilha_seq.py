# Problema valendo 2 pontos
# Implemente as funcionalidades faltantes da pilha sequencial.
# Complete o código abaixo onde é pedido

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
        return False
    pilha.elementos[pilha.tamanho] = elemento
    pilha.tamanho += 1
    return True


# Remove o elemento do topo da pilha
# Retorna True se o elemento foi removido, False caso contrário
# Complexidade esperada: O(1)
def remover(pilha: Pilha) -> bool:
    if pilha.tamanho == 0:
        return False
    pilha.tamanho -= 1
    pilha.elementos[pilha.tamanho] = None
    return True


# Exibe os elementos da pilha
# Complexidade: O(n)
def imprimir(pilha: Pilha) -> None:
    print("Base:", pilha.elementos[:pilha.tamanho], "<-topo")


# Testando a pilha #
pilha = Pilha()
inserir(pilha, 10)
inserir(pilha, 20)
inserir(pilha, 30)
inserir(pilha, 40)
imprimir(pilha)
print("Pilha esperada: 10, 20, 30, 40")
remover(pilha)
remover(pilha)
inserir(pilha, 50)
inserir(pilha, 60)
print("Pilha esperada: 10, 20, 50, 60")
imprimir(pilha)


