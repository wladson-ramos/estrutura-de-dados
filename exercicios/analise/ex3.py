from typing import List

# Ordenado
# Verifica se a lista está ordenada de forma crescente.
# Retorna True se estiver ordenada, False caso contrário.
# Lembrete: uma lista vazia é considerada ordenada.

def ordenado(lista: List[int]) -> bool:
    for i in range(1, len(lista)):
        if lista[i] < lista[i - 1]:
            return False
    return True
