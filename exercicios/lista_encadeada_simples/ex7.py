class No:
    def __init__(self, chave: int, proximo):
        self.chave = chave
        self.proximo = proximo

class ListaEncSimples:
    def __init__(self):
        self.cabeca = None

# Insere um elemento no início da lista
# Retorna True se a inserção for bem sucedida
# Complexidade esperada: O(1)
def inserir_inicio(lista: ListaEncSimples, chave: int) -> bool:
    novo_no = No(chave, lista.cabeca)
    lista.cabeca = novo_no
    return True


# Insere um elemento no fim da lista
# Retorna True se a inserção for bem sucedida
# Complexidade esperada: O(n)
def inserir_fim(lista: ListaEncSimples, chave: int) -> bool:
    novo_no = No(chave, None)
    if lista.cabeca is None:
        lista.cabeca = novo_no
        return True
    atual = lista.cabeca
    while atual.proximo is not None:
        atual = atual.proximo
    atual.proximo = novo_no
    return True