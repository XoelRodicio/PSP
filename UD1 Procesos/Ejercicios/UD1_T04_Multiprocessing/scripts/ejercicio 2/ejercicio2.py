import multiprocessing
import random

def agregar_clave(diccionario_compartido, id_proceso):
    clave = f"proceso_{id_proceso}"
    valor = random.randint(1, 100) 

    diccionario_compartido[clave] = valor
    print(f"Proceso {id_proceso} añadió: {clave} = {valor}")

if __name__ == '__main__':
    cantidad_procesos = random.randint(1,10)
    
    with multiprocessing.Manager() as manager:
        diccionario = manager.dict()
        procesos = []

        for i in range(cantidad_procesos):
            p = multiprocessing.Process(target=agregar_clave, args=(diccionario, i))
            procesos.append(p)
            p.start()  

        for p in procesos:
            p.join()

        print(f"\nDiccionario final: {dict(diccionario)}")
