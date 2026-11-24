import random
import threading
import time


class MiHilo(threading.Thread):

    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.tiempo = random.randint(0, 10000)

    def run(self):
        print(
            f"El {self.nombre} va a estar dormido durante"
            f" {self.tiempo} milisegundos."
        )

        try:
            time.sleep(self.tiempo / 1000.0)
        except Exception as e:
            print(f"Error o interrupción: {e}")

        print(f"{self.nombre} ha despertado")


if __name__ == "__main__":
    hilo1 = MiHilo("hilo1")
    hilo2 = MiHilo("hilo2")
    hilo3 = MiHilo("hilo3")

    hilo1.start()
    hilo2.start()
    hilo3.start()
