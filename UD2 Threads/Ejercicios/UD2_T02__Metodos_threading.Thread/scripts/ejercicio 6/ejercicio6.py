import threading

class Factorial(threading.Thread):
    def __init__(self, x):
        super().__init__()
        self.x = x
        self.resultado = None

    def calculo(self, x):
        if x == 0:
            return 1
        return x * self.calculo(x - 1)

    def run(self):
        print(f"empieza el proceso ... cálculo del factorial de: {self.x}")
        self.resultado = self.calculo(self.x)
        print(f"acabó el proceso ... el factorial de: {self.x} es {self.resultado}")


if __name__ == "__main__":
    for num in range(5, 9):
        hilo = Factorial(num)

        hilo.start()
        hilo.join()

    print("\nFin del ejercicio")
