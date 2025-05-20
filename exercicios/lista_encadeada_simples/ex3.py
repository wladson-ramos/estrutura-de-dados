class No:
    def __init__(self, chave: int, proximo):
        self.chave = chave
        self.proximo = proximo

class ListaEncSimples:
    def __init__(self):
        self.cabeca = None

# Retorna True se a lista estiver vazia
# Retorna False caso contrário
# Complexidade esperada: O(1)
def vazia(lista: ListaEncSimples) -> bool:
    return lista.cabeca is None
