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


# Retorna se a árvore está vazia
# Complexidade esperada: O(1)
def vazia(arv: ArvoreBinaria) -> bool:
    return arv.raiz is None

# Retorna o tamanho da árvore binária
# Complexidade esperada: O(n)
def tamanho(arv: ArvoreBinaria) -> int:
    def contar_nos(no: No) -> int:
        if no is None:
            return 0
        return 1 + contar_nos(no.esq) + contar_nos(no.dir)
    
    return contar_nos(arv.raiz)
