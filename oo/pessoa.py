class Pessoa():
    olhos = 2 #atributo de classe fica sendo um valor defaut

    # metodo é executado quando constroi o objeto
    def __init__(self, *filhos, nome = None, idade=31): #nome é um valor nulo
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod #decorator
    def metodo_statico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - Olhos da classe {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar() # super() pega a classe da classe a classe master
        return  f'{cumprimentar_da_classe}. Aperto de mão'

if __name__=='__main__':
    cleidson = Homem(nome='Cleidson')
    zeus = Pessoa(cleidson, nome='Zeus')

    print(zeus.nome)
    print(zeus.idade)
    for filho in zeus.filhos:
        print(filho.nome)

    print(cleidson.__dict__) #dunder dict mostra os atributos do objeto
    print(zeus.__dict__)

    print(Pessoa.nome_e_atributos_de_classe())

    print('___________________________________________')
    pessoa = Pessoa('Anonimo')

    # isinstance verifica se um objeto é determinada classe
    print(isinstance(pessoa, Pessoa)) # verdade
    print(isinstance(cleidson, Pessoa))  # verdade
    print(isinstance(pessoa, Homem))  # falso
    print(isinstance(cleidson, Homem))  # verdade

    print('___________________________________________')
    print('__________Sobrescrita__de__Metodo__________')



