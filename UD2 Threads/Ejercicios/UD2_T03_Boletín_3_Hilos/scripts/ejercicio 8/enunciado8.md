Ejercicio 8: Lanzamiento con Retraso Coordinado
Escenario: Un sistema de misiles defensivo requiere que 3 satélites de rastreo (Sat-A, Sat-B, Sat-C) reporten su estado a un punto de encuentro exactamente 10 segundos después de que el sistema central reciba la orden de rastreo. El sistema no puede proceder a la fase de disparo hasta que los 3 satélites hayan reportado su estado.
Problema a Simular:
El hilo principal da la orden.
Cada hilo Satélite debe usar un Timer para garantizar que su función de "reporte de estado" se active 10 segundos después.
El reporte de estado debe ser sincronizado.
Requisito de Simulación:
Combina el Timer para el inicio diferido y la Barrier para asegurar que la fase de Disparo no comience hasta que los tres reportes (activados por los Timers) hayan sido recibidos.
