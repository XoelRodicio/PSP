# ejemplo de uso: python measure_command.py ping as.com
# sañida esperada
# Ejecutando: python tarea.py
# Salida del proceso:

# Respuesta desde 2.20.253.78: bytes=32 tiempo=16ms TTL=54
# Respuesta desde 2.20.253.78: bytes=32 tiempo=15ms TTL=54
# Respuesta desde 2.20.253.78: bytes=32 tiempo=15ms TTL=54
# Respuesta desde 2.20.253.78: bytes=32 tiempo=15ms TTL=54

# Estadísticas de ping para 2.20.253.78:
#    Paquetes: enviados = 4, recibidos = 4, perdidos = 0
#    (0% perdidos),
# Tiempos aproximados de ida y vuelta en milisegundos:
#    Mínimo = 15ms, Máximo = 16ms, Media = 15ms

# Tarea terminada

# Tiempo de ejecución: 2.01 segundos
# Código de salida: 0

import sys
import subprocess
import time

argumentos = sys.argv[1:]

print(f"""
Ejecutando: {" ".join(argumentos)}
Salida del proceso:""")
inicio = time.perf_counter()
resultado = subprocess.run(argumentos, shell=True)
fin = time.perf_counter()

print(f"""
Tarea terminada

Tiempo de ejecución: {(fin - inicio):2.2f} segundos
Código de salida: {resultado.returncode}
""")