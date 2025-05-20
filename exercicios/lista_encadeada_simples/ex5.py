class No:
    def __init__(self, chave: int, proximo):
        self.chave = chave
        self.proximo = proximo

class ListaEncSimples:
    def __init__(self):
        self.cabeca = None

# Retorna o penultimo elmento da lista
# Ou None se não houver penultimo
# Complexidade esperada: O(n)
def penultimo(lista: ListaEncSimples) -> No:
    if lista.cabeca is None or lista.cabeca.proximo is None:
        return None
    atual = lista.cabeca
    while atual.proximo.proximo is not None:
        atual = atual.proximo
    return atual