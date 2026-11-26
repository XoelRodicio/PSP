import threading

class MiHilo(threading.Thread):
    saldo_actual = 2000

    def __init__(self, cantidad, nombre):
        super().__init__(target=self.retirar)  
        self.cantidad = cantidad
        self.nombre = nombre

    def retirar(self):

        print(f"{self.nombre} está intentando sacar {self.cantidad}€")

        if self.cantidad > MiHilo.saldo_actual:
            print("No dispone del saldo insuficiente para poder retirar")
        else:
            print(f"{self.nombre} sacó correctamente {self.cantidad}€")


if __name__ == "__main__":

    hilo1 = MiHilo(1500,"Yo")
    hilo1.start()
    hilo1.join()