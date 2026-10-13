2. mini_shell.py: un pequeño intérprete de comandos con alias
Queremos construir una pequeña utilidad que permita ejecutar programas desde una consola propia.
Además, queremos poder definir alias para aquellos comandos que utilizamos habitualmente.
Los alias se almacenarán en un fichero de texto:
aliases.txt

Por ejemplo:
py=python
ip=ipconfig
ping=ping -c1

Nuestro programa deberá leer estos alias al iniciarse y, posteriormente, permitir introducir comandos.
Ejemplo de utilización
Partiendo de un fichero:
aliases.txt

con:
py=python
ip=ipconfig

podremos ejecutar:
python mini_shell.py

y utilizarlo de la siguiente manera:
MiniShell
Escribe 'exit' para terminar.

> ip

Configuración de IP de Windows
...

> py hola.py

Hola

> python hola.py

Hola

> exit

Saliendo...

Si se introduce un comando que no está definido como alias, deberá intentarse ejecutar directamente.
Por ejemplo:
> ping localhost

deberá ejecutar:
ping localhost

Fichero de alias
Cada línea del fichero tendrá el formato:
alias=comando

También se permitirán argumentos en la definición:
py=python

El comando que introduzca el usuario podrá añadir argumentos.
Por ejemplo:
> py programa.py 10

deberá terminar ejecutando conceptualmente:
python programa.py 10

Requisitos del programa
El mini-shell deberá:
Leer los alias al comenzar.
Mostrar un indicador de entrada.
Leer comandos introducidos por el usuario.
Separar el nombre del comando de sus argumentos.
Comprobar si el comando es un alias.
Sustituirlo por el comando correspondiente cuando sea necesario.
Ejecutar el proceso.
Mostrar su salida estándar.
Mostrar los errores producidos por el proceso.
Continuar aceptando comandos hasta que el usuario introduzca:
exit
El mini-shell no deberá implementar:
tuberías (|);
redirecciones (>, >>);
operadores && o ||;
ejecución en segundo plano;
comillas para agrupar argumentos;
alias encadenados;
comandos internos propios del shell.
Los comandos se ejecutarán directamente mediante subprocess; no se utilizará shell=True.
Guía de desarrollo
Los argumentos que recibe el propio programa están disponibles mediante:
import sys

sys.argv

Para ejecutar un proceso:
resultado = subprocess.run(
    argumentos,
    capture_output=True,
    text=True
)

Puedes comprobar cómo ha terminado mediante:
resultado.returncode
y acceder a:
resultado.stdout
resultado.stderr

Para construir la lista de argumentos a partir de una línea sencilla puedes utilizar:
partes = linea.split()

