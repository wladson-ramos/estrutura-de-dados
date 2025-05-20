class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Conjunto:
    def __init__(self):
        self.inicio = None

    # O(n)
    def pertence(self, elem):
        atual = self.inicio
        while atual:
            if atual.valor == elem:
                return True
            atual = atual.proximo
        return False

    # O(n)
    def inserir(self, elem):
        if not self.pertence(elem):
            novo = No(elem)
            novo.proximo = self.inicio
            self.inicio = novo

    # O(n)
    def remover(self, elem):
        atual = self.inicio
        anterior = None

        while atual:
            if atual.valor == elem:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.inicio = atual.proximo
                return
            anterior = atual
            atual = atual.proximo

    # O(n)
    def imprimir(self):
        elementos = []
        atual = self.inicio
        while atual:
            elementos.append(atual.valor)
            atual = atual.proximo
        print("{", ", ".join(map(str, elementos)), "}")

    # O(n*m)
    def uniao(self, outro):
        resultado = Conjunto()
        atual = self.inicio
        while atual:
            resultado.inserir(atual.valor)
            atual = atual.proximo

        atual = outro.inicio
        while atual:
            resultado.inserir(atual.valor)
            atual = atual.proximo

        return resultado

    # O(n*m)
    def intersecao(self, outro):
        resultado = Conjunto()
        atual = self.inicio
        while atual:
            if outro.pertence(atual.valor):
                resultado.inserir(atual.valor)
            atual = atual.proximo
        return resultado

    # O(n*m)
    def diferenca(self, outro):
        resultado = Conjunto()
        atual = self.inicio
        while atual:
            if not outro.pertence(atual.valor):
                resultado.inserir(atual.valor)
            atual = atual.proximo
        return resultado


# Teste das operações

A = Conjunto()
B = Conjunto()


A.inserir(1)
A.inserir(2)
A.inserir(3)


B.inserir(3)
B.inserir(4)
B.inserir(5)

print("Conjunto A:")
A.imprimir()
print("Conjunto B:")
B.imprimir()

print("2 pertence a A?", A.pertence(2))
print("5 pertence a A?", A.pertence(5))

print("\nRemovendo elemento 2 de A")
A.remover(2)
A.imprimir()

print("\nUnião de A e B:")
uniao = A.uniao(B)
uniao.imprimir()

print("\nInterseção de A e B:")
inter = A.intersecao(B)
inter.imprimir()

print("\nDiferença A - B:")
diff = A.diferenca(B)
diff.imprimir()
