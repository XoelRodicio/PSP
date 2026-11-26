Ejercicio 2: Las Tres Cabinas de Prueba
Escenario: Una tienda de ropa tiene 8 clientes esperando, pero solo dispone de 3 cabinas de prueba (probadores).
Problema a Simular:
Define la capacidad máxima del recurso limitado (3 cabinas).
Crea una función cliente(id_cliente) que simule:
El cliente esperando a que una cabina se libere.
El cliente usando la cabina por un tiempo aleatorio (2 a 5 segundos).
El cliente liberando la cabina.
Requisito de Simulación:
Lanza 8 hilos (cliente).
Utiliza un semáforo (Semaphore) para controlar estrictamente que no haya más de 3 hilos dentro del proceso de "usar la cabina" al mismo tiempo.
