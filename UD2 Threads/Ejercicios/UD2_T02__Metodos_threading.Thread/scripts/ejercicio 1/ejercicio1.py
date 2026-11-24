import threading
import time

class MiHilo(threading.Thread):
    def run(self):
        try:
            time.sleep(2)
        except Exception as e:
            print(f"Error en el hilo: {e}")

hilo = MiHilo()

print("Antes de iniciar:", hilo.is_alive())

hilo.start()

print("Durante la ejecución:", hilo.is_alive())

hilo.join()

print("Después de join():", hilo.is_alive())
