class Pessoa():

    # metodo é executado quando constroi o objeto
    def __init__(self, nome = None, idade=31): #nome é um valor nulo
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__=='__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'fulnao'
    print(p.nome)
    print(p.idade)