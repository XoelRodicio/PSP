Ejercicio 5: La Cadena de Montaje
Escenario: En una pequeña fábrica, un hilo ("Ensamblador") produce 10 piezas que son almacenadas en un almacén temporal (búfer de capacidad limitada). Otro hilo ("Empaquetador") espera y recoge esas piezas para empaquetarlas.
Problema a Simular:
Define un búfer (lista) de capacidad 5.
El Ensamblador debe esperar si el búfer está lleno.
El Empaquetador (Consumidor) solo puede extraer piezas si el tamaño del búfer es igual o mayor a 2 (len(búfer) >= 2). El empaquetador empaqueta las piezas de 2 en 2. Si no se cumple, debe esperar.
Requisito de Simulación:
Implementa el patrón Productor-Consumidor utilizando un solo objeto Condition (Condition) para la gestión de la espera de ambas partes (wait() y notify_all()).
El consumidor debe verificar su condición de espera con: while len(búfer) < 2: junto con condition.wait().
El Ensamblador debe notificar al Empaquetador cada vez que inserte una pieza.
