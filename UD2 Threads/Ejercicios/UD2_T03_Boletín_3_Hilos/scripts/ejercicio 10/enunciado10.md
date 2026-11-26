Ejercicio 10: Venta de entradas
Diseña un programa en Python que simule la gestión de un punto de venta con tres terminales que acceden a un objeto Cajero que mantiene la cuenta de las localidades vendidas. 
Clase Cajero → es el recurso compartido por los terminales (sección crítica) 
Atributo localidades que contiene la cuenta de las localidades disponibles y vendidas 
Método retirarEntrada que irá contando las entradas vendidas 
Método mostrarLocalidades que nos dirá cuántas localidades se vendieron y cuantas quedan disponibles.
El Constructor simplemente inicializa el cajero con un nombre, un número de localidades disponibles y un tiempo límite de venta, momento en el que generará un evento (variable global) de cierre de ventas.  
Clase Terminal → (que es un hilo), en su constructor se le pasará un objeto Cajero, que será al que accede y su nombre. 
Método run(): mientras sea posible (aún no se ha generado el cierre de ventas) irá vendiendo localidades y anotando la venta general de localidades y la suya propia. Tras cada venta dormirá un tiempo aleatorio entre 1 y 10 milisegundos. 
Cuando acabe mostrará cuántas localidades vendió. 
__main__ → es el programa principal desde el que creamos un cajero, 3 terminales que trabajen con ese cajero, ponemos en funcionamiento los 3 terminales y cuando termine el tiempo de ventas se mostrará un mensaje con las localidades totales vendidas por cada terminal y las disponibles.
