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

# Retorna se o alvo está presente na árvore binária
# A função deve retornar True se a chave for encontrada, caso contrário, False.
# Complexidade esperada: O(n)
def buscar(arv: ArvoreBinaria, alvo: int) -> bool:
    def buscar_recursivo(no: No, alvo: int) -> bool:
        if no is None:
            return False
        if no.chave == alvo:
            return True
        return buscar_recursivo(no.esq, alvo) or buscar_recursivo(no.dir, alvo)

    return buscar_recursivo(arv.raiz, alvo)


