class Noarvore:
    def __init__(self, chave = None, esquerda = None, direita = None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

if __name__ == '__main__':
    raiz = Noarvore(55)
    raiz.esquerda = Noarvore(35)
    raiz.direita = Noarvore(75)

    raiz.direita.esquerda = Noarvore(65)
    raiz.direita.direita = Noarvore(85)
    raiz.esquerda.esquerda = Noarvore(25)
    raiz.esquerda.direita = Noarvore(45)

