import threading

class Factorial(threading.Thread):
    def __init__(self, numero):
        super().__init__(target=self.factorial)
        self.numero = numero
        self.resultado = None

    def recursivo(self, num):
        if num == 0:
            return 1
        return num * self.recursivo(num - 1)

    def factorial(self):
        if self.numero < 0:
            print("El número debe ser mayor o igual a 0")
        self.resultado = self.recursivo(self.numero)
        print(f"Factorial de {self.numero} = {self.resultado}")


class Fibonacci(threading.Thread):
    def __init__(self, numero):
        super().__init__(target=self.fibonacci)
        self.numero = numero
        self.resultado = None

    def recursivo(self, num):
        if num == 0:
            return 0
        elif num == 1:
            return 1
        return self.recursivo(num - 1) + self.recursivo(num - 2)

    def fibonacci(self):
        if self.numero < 0:
            print("El número debe ser mayor o igual a 0")
        self.resultado = self.recursivo(self.numero)
        print(f"Fibonacci de {self.numero} = {self.resultado}")


if __name__ == "__main__":
    numero = 6

    hilo_factorial = Factorial(numero)
    hilo_fibonacci = Fibonacci(numero)

    hilo_factorial.start()
    hilo_fibonacci.start()

    hilo_factorial.join()
    hilo_fibonacci.join()
