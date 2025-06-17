from typing import List

# Arvore binaria
class No:
    def __init__(self, chave, esq=None, dir=None):
        self.chave = chave
        self.esq = esq
        self.dir = dir

# Árvore Binária de Busca (ABB)
class ABB:
    def __init__(self):
        self.raiz = None


# Retorna o menor elemento da ABB
# Se a árvore estiver vazia, retorna None
# Complexidade: O(h), onde h é a altura da árvore
def minimo(arv: ABB) -> int:
    atual = arv.raiz
    if atual is None:
        return None
    while atual.esq is not None:
        atual = atual.esq
    return atual.chave


# Retorna o maior elemento da ABB
# Se a árvore estiver vazia, retorna None
# Complexidade: O(h)
def maximo(arv: ABB) -> int:
    atual = arv.raiz
    if atual is None:
        return None
    while atual.dir is not None:
        atual = atual.dir
    return atual.chave


# Retorna verdadeiro se a chave alvo existir na ABB, falso caso contrário
# Complexidade: O(h)
def busca(arv: ABB, alvo: int) -> bool:
    atual = arv.raiz
    while atual is not None:
        if alvo == atual.chave:
            return True
        elif alvo < atual.chave:
            atual = atual.esq
        else:
            atual = atual.dir
    return False

    
# Insere um novo nó com a chave na ABB
# Retorna True se a inserção for bem-sucedida, False se a chave já existir
# Complexidade: O(h), onde h é a altura da árvore
def inserir(arv: ABB, chave: int) -> bool:
    if arv.raiz is None:
        arv.raiz = No(chave)
        return True

    atual = arv.raiz
    while True:
        if chave == atual.chave:
            return False  # Já existe
        elif chave < atual.chave:
            if atual.esq is None:
                atual.esq = No(chave)
                return True
            atual = atual.esq
        else:
            if atual.dir is None:
                atual.dir = No(chave)
                return True
            atual = atual.dir


# Remove um nó com a chave da ABB
# Retorna True se remover, False se a chave não existir na arvore
# Complexidade esperada: O(h)
def remover(arv: ABB, chave: int) -> bool:
    if busca(arv, chave) == False:
        return False
    arv.raiz = _remover_rec(arv.raiz, chave)
    return True

def _remover_rec(atual: No, chave: int) -> No:
    if chave < atual.chave:
        atual.esq = _remover_rec(atual.esq, chave)
        return atual
    if chave > atual.chave:
        atual.dir = _remover_rec(atual.dir, chave)
        return atual
    
    # Caso 1: Nó sem filhos
    if atual.esq == None and atual.dir == None:
        return None
    # Caso 2: Nó com um filho
    if atual.esq == None:
        return atual.dir
    if atual.dir == None:
        return atual.esq
    # Caso 3: Nó com dois filhos
    sucessor = minimo_rec(atual.dir)
    atual.chave = sucessor # gambiarra para trocar o nó atual pelo sucessor
    atual.dir = _remover_rec(atual.dir, sucessor)
    return atual

def minimo_rec(atual: No) -> int:
    if atual.esq is None:
        return atual.chave
    return minimo_rec(atual.esq)


# Retorna o número de nós na árvore
# Complexidade: O(n), onde n é o número de nós na árvore
def tamanho(arv: ABB) -> int:
    def contar_nos(no: No) -> int:
        if no is None:
            return 0
        return 1 + contar_nos(no.esq) + contar_nos(no.dir)
    return contar_nos(arv.raiz)
