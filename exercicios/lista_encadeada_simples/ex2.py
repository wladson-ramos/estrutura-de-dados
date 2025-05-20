class No:
    def __init__(self, chave: int, proximo):
        self.chave = chave
        self.proximo = proximo

class ListaEncSimples:
    def __init__(self):
        self.cabeca = None

# Retorna o valor do segundo elemento da lista
# Retorna None se não houver segundo elemento
# Complexidade esperada: O(1)
def segundo(lista: ListaEncSimples) -> int:
    if lista.cabeca is None or lista.cabeca.proximo is None:
        return None
    return lista.cabeca.proximo.chave
