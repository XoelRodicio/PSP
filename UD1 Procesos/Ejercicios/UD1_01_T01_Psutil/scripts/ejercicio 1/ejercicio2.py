import datetime
import json
import os
import psutil


ESTADO = {
    "running": "iniciado",
    "stopped": "parado",
    "paused": "pausado",
    "start_pending": "iniciando",
    "stop_pending": "deteniendo",
}

INICIO = {
    "automatic": "automático",
    "manual": "manual",
    "disabled": "deshabilitado",
}


def mostrar_todos():
    print(f"{'NOMBRE'} | {'PID'} | {'ESTADO'} | {'TIPO INICIO'}")
    print("----------------------------------------------------------" )

    try:
        info = servicio.as_dict()
        nombre = info.get("name", "N/A")
        pid = info.get("pid", "N/A")

        estado = ESTADO.get(info.get("status"), "unknown")
        inicio = INICIO.get(info.get("start_type"), "unknown")

        print(f"{nombre} | {pid} | {estado} | {inicio}")
    except Exception:
        continue

    print()



while True:
    print("CONSULTA DE SERVICIOS EN WINDOWS")
    print("1. Mostrar todos los servicios")
    print("2. Mostrar servicios filtrados")
    print("3. Mostrar descripción de un servicio")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        mostrar_todos()
    elif opcion == "2":
        mostrar_filtrados()
    elif opcion == "3":
        mostrar_descripcion()
    elif opcion == "4":
        print("Bye ye")
        break
    else:
        print("Opción no válida")
