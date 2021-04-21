
"""
Isto é um Doctest

Exemplo:
# testando motor
>>> motor = Motor()
>>> motor.velocidade
0
>>> motor.acelerar()
>>> motor.velocidade
1
>>> motor.acelerar()
>>> motor.velocidade
2
>>> motor.acelerar()
>>> motor.velocidade
3
>>> motor.frear()
>>> motor.velocidade
1
>>> motor.frear()
>>> motor.velocidade
0
>>> # testando direção
>>> direcao = Direcao()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_direita()
'Leste'
>>> direcao.girar_a_direita()
'Sul'
>>> direcao.girar_a_direita()
'Oeste'
>>> direcao.girar_a_direita()
'Norte'
>>> direcao.girar_a_esquerda()
'Oeste'
>>> direcao.girar_a_esquerda()
'Sul'
>>> direcao.girar_a_esquerda()
'Leste'
>>> direcao.girar_a_esquerda()
'Norte'
>>> carro = Carro(direcao, motor)
>>> carro.calcular_velocidade()
0
>>> carro.acelerar()
>>> carro.calcular_velocidade()
1
>>> carro.acelerar()
>>> carro.calcular_velocidade()
2
>>> carro.frear()
>>> carro.calcular_velocidade()
0
>>> carro.calcular_direcao()
'Norte'
>>> carro.girar_a_direita()
>>> carro.calcular_direcao()
'Leste'
>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
'Norte'
>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
'Oeste'

"""

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade = +1

    def frear(self):
        self.velocidade = -2
        self.velocidade = max(0, self.velocidade)


NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Direcao:
    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        if self.valor == NORTE:
            self.valor = LESTE
        elif self.valor == LESTE:
            self.valor = SUL
        elif self.valor == SUL:
            self.valor = OESTE
        else:
            self.valor = NORTE

    def girar_a_esquerda(self):
        if self.valor == NORTE:
            self.valor = OESTE
        elif self.valor == LESTE:
            self.valor = NORTE
        elif self.valor == SUL:
            self.valor = LESTE
        else:
            self.valor = SUL

class Carro:
    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def calcular_direcao(self):
        return self.direcao.valor

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()
