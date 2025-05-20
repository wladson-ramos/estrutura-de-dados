from typing import List

# Repetidos
# Verifica se há elementos repetidos em uma lista de inteiros.
# Retorna True se houver, False caso contrário.

def repetidos(lista: List[int]) -> bool:
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False
