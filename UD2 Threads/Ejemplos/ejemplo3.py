import threading
import time

def descargar_archivo(nombre, duracion):
    print(f"[Hilo {nombre}] Iniciando descarga...")
    time.sleep(duracion)  # Simula IO
    print(f"[Hilo {nombre}] Descarga completada.")

if __name__ == "__main__":
    hilos = []

    for i in range(3):
        hilo = threading.Thread(
            target=descargar_archivo,
            args=(f"archivo_{i}", 2)
        )
        hilos.append(hilo)
        hilo.start()

    for h in hilos:
        h.join()

    print("[Principal] Todas las descargas han finalizado.")

