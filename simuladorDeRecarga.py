import random
import time
from collections import namedtuple
import math as math
import sistemaCobranca
from sistemaCobranca import SistemaCobranca

cobranca= SistemaCobranca()

multiplicadorDeVelocidade = 100

capacidadeBateria = range(40,100, 5)
escolhaCapacidadeBateria = random.choice(capacidadeBateria)

potenciaCarregador = [7.4, 11, 22, 50, 200]
escolhaPotenciaCarregador = random.choice(potenciaCarregador)

bateria = random.randint(25, 70)
bateriaSimulada = namedtuple('Bateria', ['percent', 'power_plugged', 'secsleft'])

energiaNecessaria = escolhaCapacidadeBateria * (100 - bateria) / 100
tempoNecessario = (energiaNecessaria / escolhaPotenciaCarregador) * 3600
tempoNecessario /= multiplicadorDeVelocidade
math.trunc(tempoNecessario)

def monitorar_carregamento():
    cobranca.__init__()
    bateriaAgora = bateria

    dadosBateria = bateriaSimulada(percent=bateriaAgora, secsleft=tempoNecessario, power_plugged=True)

    tempoRestante = dadosBateria.secsleft
    try:
        while bateriaAgora < 101:

            if bateria is None:
                print("Bateria não detectada")
                break

            print("--- Monitor de Bateria ---")
            print("Porcentagem: ", format(bateriaAgora),"%")
            print(f"Tomada: {'Sim' if bateriaSimulada.power_plugged else 'Não'}")
            print(f"Tempo restante: {tempoRestante}")
            print("\n(Pressione Ctrl+C para encerrar)")

            energiaPorSegundo = (escolhaPotenciaCarregador/3600)*multiplicadorDeVelocidade
            bateriaAgora += (energiaPorSegundo / escolhaCapacidadeBateria) * 100

            if bateriaAgora > bateria:
                tempoRestante -= 1

            time.sleep(1)
        cobranca.calcularValorSessao(energiaNecessaria)
    except KeyboardInterrupt:
        print("\nRecarga encerrada antes do tempo estipulado!")

    print("Recarga completa!")

    print(f"Resumo da sessão de recarga: \nQuantidade carregada: {100-bateria}% \nTempo de carregamento: {dadosBateria.secsleft:.2f} segundos")
    fatura = cobranca.gerarFatura("João", energiaNecessaria)
    print(fatura)

if __name__ == "__main__":
    monitorar_carregamento()




