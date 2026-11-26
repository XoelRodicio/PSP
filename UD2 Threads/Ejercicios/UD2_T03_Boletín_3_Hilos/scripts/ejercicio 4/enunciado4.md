Ejercicio 4: Alarma Programada
Escenario: Necesitas programar una tarea de copia de seguridad (backup) que se ejecute una única vez 10 segundos después de que el sistema se haya iniciado por completo, independientemente de si hay otros hilos trabajando.
Problema a Simular:
Crea una función ejecutar_backup() que simplemente imprima "¡Backup realizado!"
El hilo principal lanza una tarea larga (trabajo_en_curso) que dura 15 segundos y que no debería interrumpirse.
Requisito de Simulación:
Utiliza un temporizador (Timer) para planificar la ejecución de ejecutar_backup 10 segundos después de que el programa principal comience, sin bloquear la ejecución de trabajo_en_curso.
