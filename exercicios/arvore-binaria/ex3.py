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


# Retorna a altura da árvore binária
# Complexidade esperada: O(n)
def altura(arv: ArvoreBinaria) -> int:
    def altura_rec(no: No) -> int:
        if no is None:
            return 0
        else:
            altura_esq = altura_rec(no.esq)
            altura_dir = altura_rec(no.dir)
            return 1 + max(altura_esq, altura_dir)

    return altura_rec(arv.raiz)



