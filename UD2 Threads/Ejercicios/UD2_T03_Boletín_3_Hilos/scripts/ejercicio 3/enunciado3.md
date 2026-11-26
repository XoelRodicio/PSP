Ejercicio 3: La Señal de Inicio de Carrera
Escenario: En una competición, 5 corredores se encuentran en la línea de salida. Solo pueden empezar a correr cuando la pistola de salida (el juez) da la señal.
Problema a Simular:
Crea una función corredor(nombre) donde el corredor espera indefinidamente la señal.
El hilo principal representa al Juez. El Juez debe esperar 5 segundos (para que todos los corredores se posicionen) y luego disparar la señal de inicio.
Requisito de Simulación:
Utiliza un evento (Event) para que los 5 hilos corredores se detengan y solo comiencen su ejecución después de que el hilo Juez active la señal. Muestra cómo los corredores reaccionan inmediatamente a la señal.
