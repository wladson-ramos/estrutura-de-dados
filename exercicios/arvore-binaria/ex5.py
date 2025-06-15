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


# Retorna a quantidade de folhas na árvore binária
# Folhas são nós que não possuem filhos (esquerdo e direito)
# Complexidade esperada: O(n)
def contar_folhas(arv: ArvoreBinaria) -> int:
    def contar_folhas_no(no: No) -> int:
        if no is None:
            return 0
        if no.esq is None and no.dir is None:
            return 1
        return contar_folhas_no(no.esq) + contar_folhas_no(no.dir)
    
    return contar_folhas_no(arv.raiz)


# Retorna a quantidade de nós internos na árvore binária
# Nós internos são aqueles que possuem pelo menos um filho (esquerdo ou direito)
# Complexidade esperada: O(n)
def contar_internos(arv: ArvoreBinaria) -> int:
    def contar_internos_no(no: No) -> int:
        if no is None:
            return 0
        if no.esq is not None or no.dir is not None:
            return 1 + contar_internos_no(no.esq) + contar_internos_no(no.dir)
        return 0
    
    return contar_internos_no(arv.raiz)

