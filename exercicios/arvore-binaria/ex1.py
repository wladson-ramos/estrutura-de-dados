class No:
    def __init__(self, chave, esq, dir):
        self.chave = chave
        self.esq = esq
        self.dir = dir

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

arv = ArvoreBinaria()

arv.raiz = No(4, None, None)
arv.raiz.esq = No(76, None, None)
arv.raiz.dir = No(55, None, None)
arv.raiz.esq.esq = No(34, None, None)
arv.raiz.esq.dir = No(21, None, None)


def tamanho(raiz):
    if raiz is None:
        return 0
    else:
        return 1 + tamanho(raiz.esq) + tamanho(raiz.dir)
    
def altura(raiz):
    if raiz is None:
        return 0
    else:
        altura_esq = altura(raiz.esq)
        altura_dir = altura(raiz.dir)
        return 1 + max(altura_esq, altura_dir)
    
def contar_folhas(raiz):
    if raiz is None:
        return 0
    if raiz.esq is None and raiz.dir is None:
        return 1
    return contar_folhas(raiz.esq) + contar_folhas(raiz.dir)

def contar_internos(raiz):
    if raiz is None:
        return 0
    if raiz.esq is not None and raiz.dir is not None:
        return 1 + contar_internos(raiz.esq) + contar_internos(raiz.dir)
    return 0 
    
    

## Imprimir a árvore binária
def imprimir(arv: ArvoreBinaria) -> None:
    print(_imprimir_no(arv.raiz))

def _imprimir_no(atual: No) -> str:
    if atual is None:
        return ""
    res = str(atual.chave) + "("
    res += _imprimir_no(atual.esq)
    res += ","
    res += _imprimir_no(atual.dir)
    res += ")"
    return res

imprimir(arv)
print(tamanho(arv.raiz))
print(altura(arv.raiz))
print(contar_folhas(arv.raiz))
print(contar_internos(arv.raiz))