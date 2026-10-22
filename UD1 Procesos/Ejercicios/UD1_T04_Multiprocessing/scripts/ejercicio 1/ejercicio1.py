import multiprocessing
import time
import random

def llenar_lista(lista):
    print("Llenar lista con numeros del 1 al 10")

    for i in range(0,100):
        lista[i] = i + 1
        time.sleep(random.random()/2)

    print(f"[Proceso 1]: {list(lista)}")

def producto_lista(lista):
    print("Lista multiplicada por 2")

    for i in range(0,100):
        lista[i] = lista[i] * 2
        time.sleep(random.random()/2)

    print(f"[Proceso 2]: {list(lista)}")

            
if __name__ == "__main__":

    mylist = multiprocessing.Array('i', 100)
    proceso = multiprocessing.Process(target=llenar_lista, args=(mylist,))
    proceso2 = multiprocessing.Process(target=producto_lista, args=(mylist,))

    proceso.start()
    proceso2.start()
    proceso.join()
    proceso2.join()

    print(f"Lista desde main: ︃{mylist[:]}")