from typing import List


# Lista Sequencial Estática
class ListaSeqEst:
    def __init__(self, capacidade: int):
        self.tamanho = 0                        # Quantidade atual de elementos
        self.capacidade = capacidade            # Quantidade máxima de elementos suportados
        self.elementos = [0] * capacidade       # Lista onde são salvos os elementos


# Retorna o tamanho da lista
def tamanho(lista: ListaSeqEst) -> int:
    return lista.tamanho


# Retorna se a lista está vazia
def vazia(lista: ListaSeqEst) -> bool:
    return lista.tamanho == 0


# Retorna se a lista está cheia
def cheia(lista: ListaSeqEst) -> bool:
    return lista.tamanho == lista.capacidade


# Acessa um elemento da lista pelo índice
# Retorna o elemento se o índice for válido, None caso contrário
def acessar(lista: ListaSeqEst, indice: int) -> int:
    if 0 <= indice < lista.tamanho:
        return lista.elementos[indice]
    else:
        return None

# Dado um elemento, retorna o índice do elemento na lista
# Se o elemento não estiver na lista, retorna -1
def buscar(lista: ListaSeqEst, elemento: int) -> int:
    for i in range(lista.tamanho):
        if lista.elementos[i] == elemento:
            return i
    return -1


# Insere um elemento no final da lista
# Retorna True se o elemento foi inserido, False caso contrário
def inserir_final(lista: ListaSeqEst, elemento: int) -> bool:
    if cheia(lista):
        return False
    lista.elementos[lista.tamanho] = elemento
    lista.tamanho += 1
    return True


# Insere um elemento no início da lista
# Retorna True se o elemento foi inserido, False caso contrário
def inserir_inicio(lista: ListaSeqEst, elemento: int) -> bool:
    if cheia(lista):
        return False
    # Afasta todos elementos para a direita
    for i in range(lista.tamanho, 0, -1):
        lista.elementos[i] = lista.elementos[i - 1]
    # Coloca o novo elemento na primeira posição e atualiza tamanho
    lista.elementos[0] = elemento
    lista.tamanho += 1
    return True

# Remove o ultimo elemento da lista
# Retorna True se o elemento foi removido, False caso contrário
def remover_final(lista: ListaSeqEst) -> bool:
    if vazia(lista):
        return False
    lista.tamanho -= 1
    return True


# Remove o elemento no início da lista
# Retorna True se o elemento foi removido, False caso contrário
def remover_inicio(lista: ListaSeqEst) -> bool:
    if vazia(lista):
        return False
    # Desloca todos os elementos para a esquerda
    for i in range(1, lista.tamanho):
        lista.elementos[i-1] = lista.elementos[i]
    lista.tamanho -= 1
    return True


# Exibe os elementos da lista
def imprimir(lista: ListaSeqEst) -> None:
    print("Lista: [ ", end="")
    for i in range(lista.tamanho):
        print(lista.elementos[i], end=" ")
    print("]")
