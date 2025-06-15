from typing import List

# Arvore binaria
class No:
    def __init__(self, chave, esq, dir):
        self.chave = chave
        self.esq = esq
        self.dir = dir

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

# Retorna o menor elemento da árvore binária
# Caso a árvore esteja vazia, deve retornar None
# Complexidade esperada: O(n)
def minimo(arv: ArvoreBinaria) -> int:
    def encontrar_min(no: No) -> int:
        if no is None:
            return float('inf')
        return min(no.chave, encontrar_min(no.esq), encontrar_min(no.dir))
    
    if arv.raiz is None:
        return None
    return encontrar_min(arv.raiz)


# Retorna o menor elemento da árvore binária
# Caso a árvore esteja vazia, deve retornar None
# Complexidade esperada: O(n)
def maximo(arv: ArvoreBinaria) -> int:
    def encontrar_max(no: No) -> int:
        if no is None:
            return float('-inf')
        return max(no.chave, encontrar_max(no.esq), encontrar_max(no.dir))
    
    if arv.raiz is None:
        return None
    return encontrar_max(arv.raiz)
