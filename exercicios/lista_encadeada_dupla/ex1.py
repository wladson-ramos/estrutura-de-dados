class No:
    def __init__(self, chave: int, anterior, proximo):
        self.chave = chave
        self.anterior = anterior
        self.proximo = proximo

class ListaEncDupla:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

# Insere um elemento no início da lista
# Retorna True se a inserção for bem sucedida
# Complexidade esperada: O(1)
def inserir_inicio(lista: ListaEncDupla, chave: int) -> bool:
    novo_no = No(chave, None, None)
    if lista.cabeca is None:
        lista.cabeca = novo_no
        lista.cauda = novo_no
    else:
        novo_no.proximo = lista.cabeca
        lista.cabeca.anterior = novo_no
        lista.cabeca = novo_no
    return True




# Insere um elemento no fim da lista
# Retorna True se a inserção for bem sucedida
# Complexidade esperada: O(1)
def inserir_fim(lista: ListaEncDupla, chave: int) -> bool:
    novo_no = No(chave, None, None)
    if lista.cauda is None:
        lista.cabeca = novo_no
        lista.cauda = novo_no
    else:
        novo_no.anterior = lista.cauda
        lista.cauda.proximo = novo_no
        lista.cauda = novo_no
    return True