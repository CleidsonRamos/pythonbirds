from unittest import TestCase
from oo.carro import Motor

# esta herdando TestCase que pertence ao pacote unittest que já vem no python
class CarroTesteCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade) # verifica se o motor consegue receber zero

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)

    def teste_frear(self):
        motor = Motor()
        motor.frear()
        self.assertEqual(0, motor.velocidade)
