import random
import math


class SistemaCobranca:
    def __init__(self):
        self.tarifa = [0.70,0.75,0.80,0.85,0.90]
        self.escolherValoresTarifa = random.choice(self.tarifa)
        self.historico = []

    def calcularValorSessao(self, energiaNecessaria: float):
        custo = energiaNecessaria * self.escolherValoresTarifa
        self.historico.append(custo)
        return custo

    def gerarFatura(self, nomeCliente: str, energiaNecessaria: float):
        custo = self.calcularValorSessao(energiaNecessaria)
        return  f"Fatura de {nomeCliente}: {energiaNecessaria} kWh = R$ {custo:.2f}"

    def gerarHistorico(self):
        return sum(self.historico)