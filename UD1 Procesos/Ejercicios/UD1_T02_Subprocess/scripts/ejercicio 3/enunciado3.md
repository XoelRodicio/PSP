3. check_repo.py: comprobar el estado de un repositorio Git
Durante el trabajo habitual con Git realizamos frecuentemente una serie de operaciones en secuencia:
git status
git log
git fetch

Queremos crear una pequeña utilidad que automatice esta comprobación y presente la información de una forma más sencilla.
El programa deberá ejecutar tres comandos Git consecutivamente y elaborar un pequeño informe en castellano sobre el estado del repositorio.
Ejemplo de utilización
Desde el directorio de un repositorio:
python check_repo.py

Una posible salida sería:
========================================
COMPROBACIÓN DEL REPOSITORIO
========================================

Estado del repositorio:
Repositorio limpio.

Último commit:
8f31a2c Añadido ejercicio de subprocess

Actualización del repositorio remoto:
Fetch realizado correctamente.

========================================
RESUMEN
========================================

El repositorio no tiene cambios pendientes.
La información del repositorio remoto se ha actualizado.

Si existen archivos modificados, por ejemplo:
M calculadora.py
?? prueba.py

el programa deberá ser capaz de reconocer que existen cambios pendientes y mostrar algo similar a:
Estado del repositorio:
Hay cambios pendientes.

Archivos afectados:
  calculadora.py
  prueba.py

Comandos que debe ejecutar
El programa deberá ejecutar, en este orden:
git status --porcelain
git log -1 --oneline
git fetch origin main

El programa deberá analizar la información obtenida y generar un resumen comprensible para el usuario.
Guía de desarrollo
El programa deberá:
Comprobar que se encuentra en un repositorio Git.
Obtener el estado de los archivos.
Obtener información sobre el último commit.
Actualizar la información procedente de origin/main.
Comprobar el código de salida de cada proceso.
Analizar la salida estándar de los comandos.
Mostrar un resumen en castellano.
Si uno de los comandos produce un error, deberá informarse al usuario y no será necesario continuar con las operaciones posteriores.
El programa no tendrá que:
realizar commit;
realizar push;
realizar pull;
modificar archivos;
resolver conflictos;
analizar el historial completo;
comparar ramas distintas de main;
interpretar los mensajes de error de Git para determinar su causa exacta.
Pistas
Los tres comandos pueden ejecutarse de forma independiente:
resultado = subprocess.run(
    ["git", "status", "--porcelain"],
    capture_output=True,
    text=True
)

Puedes comprobar si el proceso ha terminado correctamente:
if resultado.returncode == 0:
    ...

La salida puede analizarse utilizando métodos habituales de las cadenas:
lineas = resultado.stdout.splitlines()

Para el último commit:
["git", "log", "-1", "--oneline"]

Y para actualizar la información del repositorio remoto:
["git", "fetch", "origin", "main"]

Ampliación
Al trabajar en un repositorio local, esta secuencia de comandos [status, log, fetch] nos permite averiguar si el repositorio local se encuentra actualizado respecto al repositorio remoto origin comprobando el último commit del repositorio local, 

git log -1 --oneline

y el último commit del repositorio remoto. 

git log -1 --oneline origin/main
