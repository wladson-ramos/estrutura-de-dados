TAMANHO_MAXIMO = 100


class Conjunto:
    def __init__(self):
        self.dados = [None] * TAMANHO_MAXIMO
        self.tamanho = 0

    # O(1) melhor caso, O(n) pior caso
    def pertence(self, elem):
        for i in range(self.tamanho):
            if self.dados[i] == elem:
                return True
        return False

    # O(n)
    def inserir(self, elem):
        if self.tamanho >= TAMANHO_MAXIMO:
            print("Conjunto cheio!")
            return
        if not self.pertence(elem):
            self.dados[self.tamanho] = elem
            self.tamanho += 1

    # O(n)
    def remover(self, elem):
        for i in range(self.tamanho):
            if self.dados[i] == elem:
                for j in range(i, self.tamanho - 1):
                    self.dados[j] = self.dados[j + 1]
                self.dados[self.tamanho - 1] = None
                self.tamanho -= 1
                return

    # O(n)
    def imprimir(self):
        print("{", end=" ")
        for i in range(self.tamanho):
            print(self.dados[i], end=" ")
        print("}")

    # O(n + m)
    def uniao(self, outro):
        resultado = Conjunto()
        for i in range(self.tamanho):
            resultado.inserir(self.dados[i])
        for i in range(outro.tamanho):
            resultado.inserir(outro.dados[i])
        return resultado

    # O(n * m)
    def intersecao(self, outro):
        resultado = Conjunto()
        for i in range(self.tamanho):
            if outro.pertence(self.dados[i]):
                resultado.inserir(self.dados[i])
        return resultado

    # O(n * m)
    def diferenca(self, outro):
        resultado = Conjunto()
        for i in range(self.tamanho):
            if not outro.pertence(self.dados[i]):
                resultado.inserir(self.dados[i])
        return resultado




# Teste das operações

if __name__ == "__main__":
    A = Conjunto()
    B = Conjunto()

    print("Inserindo elementos em A:")
    for elem in [1, 2, 3, 4, 5]:
        A.inserir(elem)
    A.imprimir()  

    print("\nInserindo elementos em B:")
    for elem in [4, 5, 6, 7, 8]:
        B.inserir(elem)
    B.imprimir()  

    print("\n3 pertence A?", A.pertence(3))
    print("10 pertence A?", A.pertence(10))

    print("\nRemovendo 3 de A")
    A.remover(3)
    A.imprimir()  

    print("\nUnião de A e B:")
    uniao = A.uniao(B)
    uniao.imprimir() 

    print("Interseção de A e B:")
    intersecao = A.intersecao(B)
    intersecao.imprimir()  

    print("Diferença de A - B:")
    diferenca = A.diferenca(B)
    diferenca.imprimir()  


    print("\nUnião de A e B:")
    uniao = A.uniao(B)
    uniao.imprimir()

    print("Interseção de A e B:")
    intersecao = A.intersecao(B)
    intersecao.imprimir()

    print("Diferença de A - B:")
    diferenca = A.diferenca(B)
    diferenca.imprimir()
