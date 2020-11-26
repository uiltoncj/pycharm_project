
#
#
# """
# Você deve criar uma classe carro que vai possuir dois atributos compostos
# por outras duas classes.
#
# 1)Motor
# 2)Direção
#
# O Motor terá responsabilidade de controlar a velocidade.
# Ele terá os seguintes atributos;
# 1)Atributo de velocidade
# 2)Método acelerar que deverar incrementar a velocidade de uma unidade
# 3)Método acelerar que deverar decrementar a velocidade de duas unidades
#
# A direção terá a responsabilidade de controlar a direção. Ela oferecerá os seguintes atributos:
# 1)Valor da direção com os seguintes valores possiveis: Norte, Sul, Leste, Oeste.
# 2)Metódo girar_a_direita:
# 3)Metódo girar_a_esquerda:
#
#     Exemplo:
#     >>> # Testando motor:
#     >>> motor = Motor()
#     >>> motor.velocidade
#     0
#     >>> motor.acelerar()
#     >>> motor.acelerar()
#     >>> motor.acelerar()
#     >>> motor.acelerar()
#     >>> motor.velocidade
#     4
#     >>> motor.frear()
#     >>> motor.velocidade
#     2
#     >>> motor.frear()
#     >>> motor.velocidade
#     0
#     >>> # Testando Direção
#     >>> direcao = Direcao()
#     >>> direcao.valor
#     'Norte'
#     >>> direcao.girar_a_direita()
#     >>> direcao.valor
#     'Leste'
#     >>> direcao.girar_a_direita()
#     >>> direcao.valor
#     'Sul'
#     >>> direcao.girar_a_direita()
#     >>> direcao.valor
#     'Oeste'
#     >>> direcao.girar_a_direita()
#     >>> direcao.valor
#     'Norte'
#     >>> direcao.girar_a_esquerda()
#     >>> direcao.valor
#     'Oeste'
#     >>> direcao.girar_a_esquerda()
#     >>> direcao.valor
#     'Sul'
#     >>> direcao.girar_a_esquerda()
#     >>> direcao.valor
#     'Leste'
#     >>> direcao.girar_a_esquerda()
#     >>> direcao.valor
#     'Norte'
#
#     >>> carro = Carro(direcao, motor)
#     >>> carro.calcular_velocidade()
#     0
#     >>> carro.acelerar()
#     >>> carro.calcular_velocidade()
#     1
#     >>> carro.acelerar()
#     >>> carro.calcular_velocidade()
#     2
#     >>> carro.frear()
#     >>> carro.calcular_velocidade()
#     0
#     >>> carro.calcular_a_direcao()
#     'Norte'
#     >>> carro.girar_a_direita()
#     >>> carro.calcular_a_direcao()
#     'Leste'
#     >>> carro.girar_a_esquerda()
#     >>> carro.calcular_a_direcao()
#     'Norte'
# """


Norte = 'Norte'
Sul = 'Sul'
Leste = 'Leste'
Oeste = 'Oeste'


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1
    def frear(self):
        self.velocidade -= 2
        self.velocidade =max(0,self.velocidade)

class Direcao(object):
    rotacao_a_direita={Norte:Leste, Leste:Sul, Sul:Oeste, Oeste:Norte}
    rotacao_a_esquerda={Norte:Oeste, Oeste:Sul, Sul:Leste, Leste:Norte}

    def __init__(self):
        self.valor = Norte

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda[self.valor]

class Carro:
    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao
    def calcular_velocidade(self):
        return self.motor.velocidade
    def acelerar(self):
        return self.motor.acelerar()
    def frear(self):
        return self.motor.frear()

    def calcular_a_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        return self.direcao.girar_a_direita()
    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()

