class No:
    def __init__(self, chave: int, anterior, proximo):
        self.chave = chave
        self.anterior = anterior
        self.proximo = proximo

class ListaEncDupla:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

# Remove um elemento no início da lista
# Retorna True se a remoção for bem sucedida
# Complexidade esperada: O(1)
def remover_inicio(lista: ListaEncDupla) -> bool:
    if lista.cabeca is None:
        return False
    if lista.cabeca == lista.cauda:
        lista.cabeca = None
        lista.cauda = None
    else:
        lista.cabeca = lista.cabeca.proximo
        lista.cabeca.anterior = None

    return True


# Remove um elemento no fim da lista
# Retorna True se a remoção for bem sucedida
# Complexidade esperada: O(1)
def remover_fim(lista: ListaEncDupla) -> bool:
    if lista.cauda is None:
        return False
    if lista.cauda == lista.cabeca: 
        lista.cauda = None
        lista.cabeca = None
    else:
        lista.cauda = lista.cauda.anterior
        lista.cauda.proximo = None
    return True