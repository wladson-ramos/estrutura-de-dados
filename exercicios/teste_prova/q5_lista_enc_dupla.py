# Problema valendo 2 pontos
# Implemente a função "equivalentes".
# Complete o código abaixo onde é pedido

from typing import List
class No:
    def __init__(self, chave: int, anterior, proximo):
        self.chave = chave
        self.anterior = anterior
        self.proximo = proximo

class ListaEncDupla:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

# Converte um vetor de inteiros em uma lista encadeada dupla
# Você deve ajustar os ponteiros anterior e proximo de cada nó
# Complexidade esperada: O(n)
def converte_vetor_para_LED(vetor: List[int]) -> ListaEncDupla:
    led = ListaEncDupla()
    if not vetor:
        return led

    anterior = None
    for valor in vetor:
        novo_no = No(valor, anterior, None)
        if anterior is None:
            led.cabeca = novo_no  
        else:
            anterior.proximo = novo_no
            novo_no.anterior = anterior
        anterior = novo_no

    led.cauda = anterior 
    return led




# TESTE #

vetor = [10, 20, 30, 40]
led = converte_vetor_para_LED(vetor)

print("Vetor:", vetor)
print("Lista encadeada dupla:", end=" ")

def imprimir(atual: No) -> None:
    if atual == None:
        print("None")
        return
    print(atual.chave, end=" <-> ")
    imprimir(atual.proximo)

imprimir(led.cabeca)

