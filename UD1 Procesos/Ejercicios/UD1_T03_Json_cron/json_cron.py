import json
import sys
import os
from TrabajoProgramado import TrabajoProgramado

def leer_trabajos(nombre_fichero):
    trabajos_json = []
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),nombre_fichero), "r") as fichero_trabajos:
        trabajos_json =  json.load(fichero_trabajos)

    trabajos_programados = []
    for t in trabajos_json:
        trabajoProgramado = TrabajoProgramado(**t)
        trabajos_programados.append(trabajoProgramado)

    return trabajos_programados


if __name__ == "__main__":
    # Formato de llamada correcto
    if len(sys.argv)!=2:
        print(f"Uso: python {os.path.basename(__file__)} nombre_fichero.json")
        sys.exit(1)

    nombre_fichero = sys.argv[-1]

    trabajos_programados = leer_trabajos(nombre_fichero)

    
    for t in trabajos_programados:
        t.iniciar()

    