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


# Função que verifica se a árvore binária é uma árvore binária de busca (ABB)
# Complexidade esperada: O(n), complexidade aceitável: O(n²)
def confere_abb(arv: ArvoreBinaria) -> int:
    def eh_abb(no, min_val, max_val):
        if no is None:
            return True
        if (min_val is not None and no.chave <= min_val) or (max_val is not None and no.chave >= max_val):
            return False
        return eh_abb(no.esq, min_val, no.chave) and eh_abb(no.dir, no.chave, max_val)
    
    return eh_abb(arv.raiz, None, None)

# Uma ABB é uma árvore onde para cada nó:
# - Todos os nós da subárvore esquerda possuem valores menores que o nó atual.
# - Todos os nós da subárvore direita possuem valores maiores que o nó atual.
