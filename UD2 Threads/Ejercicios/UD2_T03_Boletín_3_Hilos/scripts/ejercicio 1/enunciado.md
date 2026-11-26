Ejercicio 1: El Cajero Automático Compartido
Escenario: Tienes una cuenta bancaria (saldo_actual) y dos personas (tú y tu cónyuge) intentan realizar retiros simultáneamente desde diferentes cajeros automáticos.
Problema a Simular:
Crea la variable compartida saldo_actual con un valor inicial de 2000€.
Define una función retirar(cantidad, nombre) que simule una operación bancaria (lectura, espera, modificación).
Simula 5 retiros de 300€ y 5 retiros de 100€, lanzados de forma concurrente por los dos hilos (personas).
Requisito de Simulación:
Muestra qué sucede si no se utiliza ningún mecanismo de sincronización (la condición de carrera).
Implementa la solución utilizando el mecanismo de exclusión mutua más adecuado para garantizar que el saldo final sea correcto y que nunca se retire dinero si el saldo es insuficiente (aunque esta última verificación debe ir dentro de la región crítica).
