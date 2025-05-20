from typing import List

# Menor elemento
# Retorna o índice do menor elemento da lista.
# Caso hajam menores elementos iguais, retorna o índice do primeiro.
# Retorna -1 se a lista estiver vazia.

def menor_elemento(lista: List[int]) -> int:
    if len(lista) == 0:
        return -1

    indice_menor = 0

    for i in range(1, len(lista)):
        if lista[i] < lista[indice_menor]:
            indice_menor = i

    return indice_menor
