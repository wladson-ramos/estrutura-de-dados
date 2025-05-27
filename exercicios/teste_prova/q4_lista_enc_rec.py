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

# Conta o número de elementos pares de forma RECURSIVA
# da lista encadeada simples enraizada a partir do nó atual 
# Complexidade esperada: O(n)
def contapar_rec(atual: No) -> int:
    if atual is None:
        return 0
    return (1 if atual.chave % 2 == 0 else 0) + contapar_rec(atual.proximo)



## TESTES ##
lista1 = ListaEncSimples()
lista1.cabeca = No(1, No(2, No(3, No(4, None))))
print("Lista 1 -> 2 -> 3 -> 4")
print("Esperado: 2")
print("Resultado:", contapar_rec(lista1.cabeca))
print()

lista2 = ListaEncSimples()
lista2.cabeca = No(1, No(3, No(5, No(7, None))))
print("Lista 1 -> 3 -> 5 -> 7")
print("Esperado: 0")
print("Resultado:", contapar_rec(lista2.cabeca))
print()

lista3 = ListaEncSimples()
lista3.cabeca = None
print("Lista vazia")
print("Esperado: 0")
print("Resultado:", contapar_rec(lista3.cabeca))
print()


