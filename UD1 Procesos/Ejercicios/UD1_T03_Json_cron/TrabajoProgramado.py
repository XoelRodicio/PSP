import multiprocessing
import time
import subprocess
import os

class TrabajoProgramado:
    def __init__(self, id, comando, intervalo):
        self.id = id
        self.comando = comando
        self.intervalo = intervalo

    def ejecutar_y_cerrar(self, id, comando, intervalo):
        #diccionario de subprocesos identificados por su id+estampa de tiempo+valor autonumerico
        #el id de un subproceso en este diccionario va ligado al nombre del fichero donde se vuelca su salida
        dict_subprocesos = {}
        #el indice autonumerico evita que dos subprocesos del mismo trabajo escriban en el mismo fichero (y machaquen su contenido) si se ha definido un intervalo de un segundo
        autonumerico = 1
        while True:
            id_subproceso = id+"_"+time.strftime("%Y%m%d%H%M%S",time.localtime())+"_"+str(autonumerico)
            #Bucle infinito de lanzamiento de subprocesos con Popen. Cada subproceso se debe lanzar se manera asincrona redirigiendo su salida a un fichero previamente creado y abierto para escritura. Después de cada lanzamiento, se sodnea la lista de todos los subprocesos lanzados (no sabemos cuanto tiempo tardará en terminar de hacer su trabajo, pero asumimos que siempre será más que el tiempo que tarda en cerrarse los ficheros que estén abiertos). Al superar el bloque de sondeo se introduce una espera según el intervalo indicado para lanzar el suproceso de nuevo en la siguiente vuelta del bucle.
            fichero = open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"logs",id_subproceso+".log"),"w", encoding="utf-8")
            subproceso = subprocess.Popen(comando, text=True, stdout=fichero, stderr=subprocess.STDOUT, shell=True, encoding="utf-8")

            dict_subprocesos[id_subproceso]=(subproceso,fichero)

            for k in list(dict_subprocesos.keys()):
                (s,f) = dict_subprocesos[k]
                if s.poll() is not None:
                    f.close()
                    n_ejecucion = k[k.rfind("_")+1:]
                    print(f"Terminada ejecución {n_ejecucion} para {id}. Revisa la salida en el fichero {k+".log"}")
                    del dict_subprocesos[k]


            time.sleep(intervalo)
            autonumerico+=1
    
    
    
    def iniciar(self):
        #TODO: iniciar debe lanzar un proceso independiente que se encargue de lanzar periodicamente el comando en cuestión de manera infinita. Una vez lanzado, solo se informa desde el propio método por consola que el comando con el id definido ha sido lanzado.

        proceso_de_atencion_periodica = multiprocessing.Process(target=self.ejecutar_y_cerrar, args=(self.id, self.comando, self.intervalo))
        proceso_de_atencion_periodica.start()

        print(f"El proceso {self.id} ha sido lanzado con una frecuencia de ejecución de {self.intervalo} segundos")
        