import threading

contador = 0

class Hilo(threading.Thread):
    def __init__(self, cadena):
        super().__init__()
        self.cadena = cadena

    def run(self):
        global contador
        for _ in range(10):
            contador += 1
            print(f"{contador}:{self.cadena}", end="")

if __name__ == "__main__":
    hiloA = Hilo("SI ")
    hiloB = Hilo("NO ")

    print("Comienzo de la ejecucion concurrente")
    hiloA.start()
    hiloB.start()
    hiloA.join()
    hiloB.join()