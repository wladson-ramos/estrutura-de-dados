from typing import List

class Fila:
    def __init__(self):
        self.capacidade = 8
        self.inicio = 0
        self.tamanho = 0
        self.elementos = [None] * self.capacidade


# Retorna o elemento no início da fila
# Se a fila estiver vazia, retorna None
# Complexidade esperada: O(1)
def acessar(fila: Fila):
    if fila.tamanho == 0:
        return None
    return fila.elementos[fila.inicio]


# Retorna se a fila está vazia
# Complexidade esperada: O(1)
def vazia(fila: Fila) -> bool:
    return fila.tamanho == 0


# Insere o elemento no topo da fila
# Retorna True se o elemento foi inserido, False caso contrário
# Complexidade esperada: O(1)
def inserir(fila: Fila, elemento) -> bool:
    if fila.tamanho == fila.capacidade:
        return False 
    fim = (fila.inicio + fila.tamanho) % fila.capacidade
    fila.elementos[fim] = elemento
    fila.tamanho += 1
    return True


# Remove o elemento do topo da fila
# Retorna True se o elemento foi removido, False caso contrário
# Complexidade esperada: O(1)
def remover(fila: Fila) -> bool:
    if fila.tamanho == 0:
        return False
    fila.inicio = (fila.inicio + 1) % fila.capacidade
    fila.tamanho -= 1
    return True


# Exibe os elementos da fila
# Complexidade: O(n)
def imprimir(fila: Fila) -> None:
    print("Inicio: ", end="")
    for i in range(fila.tamanho):
        pos = (fila.inicio + i) % fila.capacidade
        if i == fila.tamanho - 1:
            print(fila.elementos[pos], end="")
        else:
            print(fila.elementos[pos], end=", ")
    print(" final")


f = Fila()
print(vazia(f))         # True

inserir(f, 1)
inserir(f, 2)
inserir(f, 3)
inserir(f, 4)

imprimir(f)             # Inicio: 1, 2, 3, 4 final
print(acessar(f))       # 1

remover(f)
imprimir(f)             # Inicio: 2, 3, 4 final

inserir(f, 5)
inserir(f, 6)
inserir(f, 7)
inserir(f, 8)
inserir(f, 9)           # Deve retornar False (fila cheia)
imprimir(f)             # Deve mostrar os 7 primeiros elementos inseridos
