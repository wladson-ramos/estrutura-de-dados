class No:
    def __init__(self, chave: int, proximo):
        self.chave = chave
        self.proximo = proximo

class ListaEncSimples:
    def __init__(self):
        self.cabeca = None

# Retorna o valor do primeiro elemento da lista
# Retorna None se a lista estiver vazia
# Complexidade esperada: O(1)
def primeiro(lista: ListaEncSimples) -> int:
    if lista.cabeca is None:
        return None
    return lista.cabeca.chave
