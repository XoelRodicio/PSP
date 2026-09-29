import psutil

def mostrar_info():
    # Plataforma
    print(f"Hola Mundo soy linux? {psutil.LINUX}")
    print(f"Hola Mundo soy windows? {psutil.WINDOWS}")

    # Información de CPUs
    print(f"Número de CPUs: {psutil.cpu_count()}")
    print(f"Frecuencia de cada CPU: {psutil.cpu_freq()}")
    print(f"Uso de CPU por CPUs: {psutil.cpu_percent()}%")
    
    # Información de memoria
    print(f"Memoria total: {psutil.virtual_memory().total} bytes")
    print(f"Memoria disponible: {psutil.virtual_memory().available} bytes")
    print(f"Porcentaje de memoria usada: {psutil.virtual_memory().percent}%")
    
    # Información de discos
    print(f"Listado de particiones: {psutil.disk_partitions()}")
    print(f"Uso de disco principal: {psutil.disk_usage('/').percent}%")
    
    print(f"Número de operaciones de lectura: {psutil.disk_io_counters().read_count}")
    print(f"Número de operaciones de escritura: {psutil.disk_io_counters().write_count}")
    print(f"Número de bytes leídos: {psutil.disk_io_counters().read_bytes}")
    print(f"Número de bytes escritos: {psutil.disk_io_counters().write_bytes}")
    
    # Estadísticas de red
    print(f"Bytes enviados: {psutil.net_io_counters().bytes_sent}")
    print(f"Bytes recibidos: {psutil.net_io_counters().bytes_recv}")
    print(f"Paquetes enviados: {psutil.net_io_counters().packets_sent}")
    print(f"Paquetes recibidos: {psutil.net_io_counters().packets_recv}")


# Guardar información del sistema:
import datetime
import json
import os

def sistema_json():
    diccionario = {
        "sistema_operativo": {
        "es_linux": psutil.LINUX,
        "es_windows": psutil.WINDOWS
        },
        "cpu": {
            "numero_cpus": psutil.cpu_count(),
            "frecuencia_mhz": psutil.cpu_freq().current if psutil.cpu_freq() else None,
            "porcentaje_uso": psutil.cpu_percent() 
        },
        "memoria": {
            "total_bytes": psutil.virtual_memory().total,
            "disponible_bytes": psutil.virtual_memory().available,
            "porcentaje_usado": psutil.virtual_memory().percent
        },
        "disco": {
            "porcentaje_uso_raiz": psutil.disk_usage('/').percent,
            "operaciones_lectura": psutil.disk_io_counters().read_count,
            "operaciones_escritura": psutil.disk_io_counters().write_count,
            "bytes_leidos": psutil.disk_io_counters().read_bytes,
            "bytes_escritos": psutil.disk_io_counters().write_bytes
        },
        "red": {
            "bytes_enviados": psutil.net_io_counters().bytes_sent,
            "bytes_recibidos": psutil.net_io_counters().bytes_recv,
            "paquetes_enviados": psutil.net_io_counters().packets_sent,
            "paquetes_recibidos": psutil.net_io_counters().packets_recv
        }
    }


# Menú
while True:
    print("1. Mostrar información del sistema")
    print("2. Guardar información del sistema")
    print("3. Salir")
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        mostrar_info()
    elif opcion == "2":
        sistema_json()
    elif opcion == "3":
        print("Bye ye")
        break
    else:
        print("Opción no válida")
