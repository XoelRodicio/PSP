import threading

class HiloYes(threading.Thread):
    def run(self):
        for i in range(30):
            print("YES ", end="")

class HiloNo(threading.Thread):
    def run(self):
        for i in range(30):
            print("NO ", end="")

if __name__ == "__main__":

    hiloA = HiloNo()
    hiloB = HiloYes()

    print("Ejecución en hilo A")
    hiloA.start()
    print("\nEjecución en hilo B")
    hiloB.start()

    hiloA.join()
    hiloB.join()

    print("\nEjecucion en main")