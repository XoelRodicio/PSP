import threading


class HiloSecuencia(threading.Thread):

  def __init__(self, inicio: int, fin: int, nombre: str):
    super().__init__()

    self.inicio = inicio
    self.fin = fin
    self.nombre = nombre

  def run(self):
    print(f"{self.nombre} Comienza la ejecución")

    for numero in range(self.inicio, self.fin + 1):
      print(f"{self.nombre}: {numero}")

    print(f"{self.nombre} Ha terminado")


# Programa principal
if __name__ == "__main__":
  thread_a = HiloSecuencia(1, 10, "ThreadA")
  thread_b = HiloSecuencia(20, 30, "ThreadB")

  print("Vamos a iniciar los dos threads")

  thread_a.start()
  thread_b.start()

  print("Los hilos se han inicializado")

  print("El programa principal ha terminado")
