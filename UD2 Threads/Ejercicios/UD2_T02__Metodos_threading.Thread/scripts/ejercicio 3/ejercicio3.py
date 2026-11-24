import threading
import time

class HiloContador(threading.Thread):

    def __init__(self, nombre):
        super().__init__(name=nombre)

    def run(self):
        for i in range(1, 101):
            time.sleep(0.1)
            print(f"Hilo ID: {self.ident} Nombre: {self.name}: Valor: {i}")

if __name__ == "__main__":
    inicio = time.perf_counter()

    hilo_secundario = HiloContador("Contador-1")
    hilo_secundario.start()
    hilo_secundario.join()

    fin = time.perf_counter()
    tiempo_total = fin - inicio

    print(f"\nEl hilo secundario ha finalizado")
    print(f"Tiempo total de ejecución: {tiempo_total} segundos")
