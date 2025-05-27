# Problema valendo 2 pontos
# Implemente a função "equivalentes".
# Complete o código abaixo onde é pedido
class No:
    def __init__(self, chave: int, proximo):
        self.chave = chave
        self.proximo = proximo

class ListaEncSimples:
    def __init__(self):
        self.cabeca = None

# Compara duas listas encadeadas simples
# As listas são equivalentes se tiverem o mesmo número de elementos
# e os mesmos elementos na mesma ordem
# Complexidade esperada: O(n + m) ou O(min(n, m))
def equivalentes(lista1: ListaEncSimples, lista2: ListaEncSimples) -> bool:
    atual1 = lista1.cabeca
    atual2 = lista2.cabeca

    while atual1 is not None and atual2 is not None:
        if atual1.chave != atual2.chave:
            return False
        atual1 = atual1.proximo
        atual2 = atual2.proximo

    return atual1 is None and atual2 is None





# TESTES #

lista1 = ListaEncSimples()
lista1.cabeca = No(10, No(20, No(30, None)))

lista2 = ListaEncSimples()
lista2.cabeca = No(10, No(20, No(30, None)))

lista3 = ListaEncSimples()
lista3.cabeca = No(10, No(20, No(55, None)))

lista4 = ListaEncSimples()
lista4.cabeca = No(10, No(20, None))

print("Esperado: True")
print("Resultado:", equivalentes(lista1, lista2))

print("Esperado: False")
print("Resultado:", equivalentes(lista1, lista3))

print("Esperado: False")
print("Resultado:", equivalentes(lista1, lista4))