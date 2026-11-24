import threading
import time

class MiHilo(threading.Thread):
    def __init__(self, tiempo_espera=2):
        super().__init__()
        self.tiempo_espera = tiempo_espera

    def run(self):
        print(f"Iniciando {self.name}")
        time.sleep(self.tiempo_espera)
        print(f"Finalizando {self.name}")

if __name__ == "__main__":
    inicio = time.perf_counter()

    hilos = []

    for i in range(1, 6):
        hilo = MiHilo()
        hilo.name = f"miHilo-{i}"
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()

    fin = time.perf_counter()
    tiempo_total = fin - inicio

    print(f"\nTodos los hilos han finalizado.")
    print(f"Tiempo total de ejecución: {tiempo_total} segundos")
