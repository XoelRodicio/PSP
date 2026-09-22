# Ejercicio 1. Demostración de ejecución

import psutil

# Plataforma sobre la que se ejecuta el script: Windows o Linux
print(f"Hola Mundo soy linux? {psutil.LINUX}")
print(f"Hola Mundo soy windows? {psutil.WINDOWS}")

# Información de CPUs
# Numero de CPUs
print(f"Numero de CPU: {psutil.cpu_times()}")

# Frecuencia de cada CPU
print(f"Frecuencia de CPU: {psutil.cpu_percent(interval=1)}")

# Número de CPU por CPU
print(f"Numero de CPU por CPU: {psutil.cpu_freq()}")

# Memoria total
# Memoria disponible
print(f"Memoria disponible: {psutil.virtual_memory().available} bytes")

# Porcentaje de memoria usada
print(f"Porcentaje de memoria usada: {psutil.virtual_memory().percent}%")

# Información de discos
# Listado de particiones
print(f"Listado de particiones: {psutil.disk_partitions()}")
print(F"Disk Usage: {psutil.disk_usage('/')}")