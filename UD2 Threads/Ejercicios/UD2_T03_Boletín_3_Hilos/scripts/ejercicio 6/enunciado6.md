Ejercicio 6: El Buscador de Tareas
Escenario: Una aplicación lee una lista de 50 URLs (tareas) desde un fichero y las distribuye a 3 hilos worker (Consumidores) que simulan el procesamiento de cada URL.
Problema a Simular:
Crea una lista de 50 tareas (URLs ficticias).
El hilo principal pone las 50 tareas en una cola segura.
Lanza 3 hilos worker. Cada worker extrae tareas de la cola hasta que esta esté vacía.
Asegura que los workers sepan cuándo terminar.
Requisito de Simulación:
Utiliza la clase queue.Queue para gestionar el paso de tareas de forma segura y automática (sin Locks ni Conditions manuales).
