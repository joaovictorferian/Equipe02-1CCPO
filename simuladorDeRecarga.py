import random
import time
from collections import namedtuple
import math as math
from sistemaCobranca import SistemaCobranca
from equacoesRecarga import equacoesRecarga

nomeCliente = input("Digite o seu nome: ")
modeloCarro = input("Qual é o seu carro: ")

bateriaSimulada = namedtuple('Bateria', ['percent', 'power_plugged', 'secsleft'])
sessao = equacoesRecarga()
cobranca = SistemaCobranca()

def monitorar_carregamento():
    sessao.iniciarEquacoes()
    bateriaAgora = sessao.bateria
    tempoNecessario = sessao.tempo

    dadosBateria = bateriaSimulada(percent=bateriaAgora, secsleft=tempoNecessario, power_plugged=True)
    try:
        statusCarregamento = True
        while bateriaAgora < 101:

            if sessao.bateria is None:
                print("Bateria não detectada")
                break

            print("--- Monitor de Bateria ---")
            print(f"Porcentagem: {bateriaAgora:.2f}%")
            print(f"Tomada: {'Sim' if dadosBateria.power_plugged else 'Não'}")
            print(f"Tempo restante: {tempoNecessario:.0f} segundos")

            energiaPorSegundo = (sessao.potencia/3600)*sessao.multiplicadorVelocidade
            bateriaAgora += (energiaPorSegundo / sessao.capacidade)*100
            energiaRestante = (100 - bateriaAgora) * sessao.capacidade / 100
            tempoRestante = (energiaRestante / energiaPorSegundo)
            tempoNecessario = tempoRestante

            time.sleep(1)
    except KeyboardInterrupt:
        print("\nRecarga encerrada antes do tempo estipulado!")
        statusCarregamento = False


    if statusCarregamento:
        print("Recarga completa!")

        print(f"Resumo da sessão de recarga: \nQuantidade carregada: {100-sessao.bateria}% \nTempo de carregamento: {sessao.tempo:.2f} segundos")
        fatura = cobranca.gerarFatura(modeloCarro, nomeCliente, sessao.energia)
        print(fatura)

if __name__ == "__main__":
    monitorar_carregamento()




