Ejercicio 9: Control de Inventario en un Almacén
Escenario: Un almacén tiene un inventario de un producto con stock inicial de 50.
Hilo 1 (Reabastecedor): Repone 10 unidades cuando el stock cae a 10 o menos.
Hilo 2 (Vendedor): Intenta vender 15 unidades.
Hilo 3 (Jefe de Turno): Cierra el sistema al final del día.
Problema a Simular:
El Vendedor debe usar un mecanismo para esperar si no hay suficiente stock.
El Reabastecedor debe notificar al Vendedor cuando haya repuesto el stock.
El Jefe de Turno debe usar un mecanismo para detener inmediatamente el bucle de venta del Vendedor.
Requisito de Simulación:
Utiliza un Lock para proteger la variable stock.
Utiliza una Condition para gestionar la espera del Vendedor (esperando stock).
Utiliza un Event para que el Jefe de Turno pueda mandar una señal de "Cierre" al Vendedor.
