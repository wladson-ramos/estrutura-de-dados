class No:
    def __init__(self, chave: int, anterior, proximo):
        self.chave = chave
        self.anterior = anterior
        self.proximo = proximo

class ListaEncDupla:
    def __init__(self):
        self.cabeca = None
        self.cauda = None


# Verifica se uma lista encadeada dupla é palíndromo
# Uma sequencia é palíndromo se ela é igual a sua reversa
# Retorna True se a lista for palíndromo, False caso contrário
# Complexidade esperada: O(n)
def palindromo(lista: ListaEncDupla) -> bool:
    esquerda = lista.cabeca
    direita = lista.cauda
    while esquerda and direita and esquerda != direita and esquerda.anterior != direita:
        if esquerda.chave != direita.chave:
            return False
        esquerda = esquerda.proximo
        direita = direita.anterior
    return True 


# Exemplo de palíndromo:
# 1 -> 2 -> 3 -> 2 -> 1
# Exemplo de não palíndromo:
# 1 -> 2 -> 3 -> 4 -> 5