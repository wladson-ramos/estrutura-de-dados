from typing import List

# Busca Linear
# Realiza uma busca em uma lista de inteiros.
# Retorna o índice do primeiro elemento encontrado.
# Retorna -1 se não encontrado.

def busca_linear(lista: List[int], alvo: int) -> int:
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1
