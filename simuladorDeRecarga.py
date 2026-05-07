import random
import time
import os
from collections import namedtuple

from sympy.physics.units import percent

bateriaSimulada = namedtuple('bateria', 'percent power_plugged secsleft')


def monitorar_carregamento():
    bateria = random.randint(25,70)
    try:
        while bateria < 100:

            bateria = bateriaSimulada(percent=bateria, secsleft=-1, power_plugged=True)

            if bateria is None:
                print("Bateria não detectada")
                break

            os.system('cls' if os.name == 'nt' else 'clear')

            print("--- Monitor de Bateria ---")
            print(f"Porcentagem: {percent}%")
            print(f"Tomada: {'Sim' if bateria.power_plugged else 'Não'}")
            print(f"Tempo restante: {bateria.secsleft}")
            print("\n(Pressione Ctrl+C para encerrar)")

            bateria+=1
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitoramento encerrado")

if __name__ == "__main__":
    monitorar_carregamento()

