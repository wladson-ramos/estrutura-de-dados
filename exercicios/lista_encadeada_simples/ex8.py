class No:
    def __init__(self, chave: int, proximo):
        self.chave = chave
        self.proximo = proximo

class ListaEncSimples:
    def __init__(self):
        self.cabeca = None

# Remove o primeiro elemento da lista
# Retorna True se a remoção for bem sucedida
# Retorna False se a lista estiver vazia
# Complexidade esperada: O(1)
def remover_inicio(lista: ListaEncSimples) -> bool:
    if lista.cabeca is None:
        return False
    lista.cabeca = lista.cabeca.proximo
    return True

# Remove o último elemento da lista
# Retorna True se a remoção for bem sucedida
# Retorna False caso contrário
# Complexidade esperada: O(n)
def remover_fim(lista: ListaEncSimples) -> bool:
    if lista.cabeca is None:
        return False
    if lista.cabeca.proximo is None:
        lista.cabeca = None
        return True
    atual = lista.cabeca
    while atual.proximo.proximo is not None:
        atual = atual.proximo
    atual.proximo = None
    return True

