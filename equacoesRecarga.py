import random
import math

class equacoesRecarga():
    def iniciarEquacoes(self):
        self.multiplicadorVelocidade = 100
        self.capacidade = self.get_capacidade()
        self.potencia = self.get_potencia()
        self.bateria = self.get_bateria()

        self.energia = self.calcularEnergiaNecessaria(self.capacidade, self.bateria)
        self.tempo = self.calcularTempoNecessario(self.energia, self.potencia)
        self.tempo = math.trunc(self.tempo)

    def get_capacidade(self):
        return random.uniform(40, 100)

    def get_potencia(self):
        return random.choice([2.5, 7.4, 22, 50])

    def get_bateria(self):
        return random.uniform(25, 75)

    def calcularEnergiaNecessaria(self, capacidade, bateria):
        return  capacidade * (100 - bateria) / 100

    def calcularTempoNecessario(self, energia, potencia):
        return ((energia / potencia) * 3600) / self.multiplicadorVelocidade



