1. measure_command.py: medir el tiempo de ejecución de un proceso
Cuando ejecutamos un programa desde una consola podemos observar cuánto tarda en finalizar, pero queremos crear una pequeña utilidad que permita medir automáticamente el tiempo empleado por otro programa.
Por ejemplo, queremos poder ejecutar:
python measure_command.py python tarea.py

y obtener información sobre cuánto tiempo ha tardado tarea.py.
Ejemplo de utilización
Si tenemos un programa:
tarea.py

que tarda unos dos segundos en ejecutarse:
python measure_command.py python tarea.py

La salida podría ser:
Ejecutando: python tarea.py
Salida del proceso:
Tarea terminada

Tiempo de ejecución: 2.01 segundos
Código de salida: 0

El tiempo exacto dependerá del ordenador y de la tarea ejecutada.
También debería ser posible pasar argumentos al programa que queremos ejecutar:
python measure_command.py python tarea.py 10

En este caso, 10 deberá llegar como argumento a tarea.py.
Requisitos del programa
El programa deberá:
Recibir mediante la línea de comandos el programa que se quiere ejecutar.
Recibir también los argumentos destinados a ese programa.
Lanzar el proceso.
Esperar a que termine.
Medir el tiempo transcurrido.
Mostrar la salida estándar producida por el proceso.
Mostrar su código de salida.
No es necesario implementar:
ejecución de varios programas;
ejecución en segundo plano;
tuberías entre programas;
redirecciones;
interpretación de comandos de un shell.
Guía de desarrollo
Los argumentos que recibe el propio programa están disponibles mediante:
import sys

sys.argv

La función que permite lanzar un proceso es:
import subprocess

resultado = subprocess.run(...)

Para recuperar la salida estándar puedes utilizar:
resultado.stdout

Si quieres trabajar con la salida directamente como texto, puedes utilizar:
subprocess.run(
    ...,
    capture_output=True,
    text=True
)

Para medir el tiempo puedes utilizar time.perf_counter():
import time

inicio = time.perf_counter()

resultado = subprocess.run(...)

fin = time.perf_counter()

El tiempo transcurrido será:
fin - inicio

