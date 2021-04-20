class Pessoa():

    # metodo é executado quando constroi o objeto
    def __init__(self, *filhos, nome = None, idade=31): #nome é um valor nulo
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__=='__main__':
    cleidson = Pessoa(nome='Cleidson')
    zeus = Pessoa(cleidson, nome='Zeus')

    print(zeus.nome)
    print(zeus.idade)
    for filho in zeus.filhos:
        print(filho.nome)
