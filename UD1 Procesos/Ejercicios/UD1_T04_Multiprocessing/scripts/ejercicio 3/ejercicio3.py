import multiprocessing
import random
import time

def generar(cola, cantidad_numeros):
    for _ in range(cantidad_numeros):
        numero = random.randint(1, 10)
        cola.put(numero)
        print(numero)

    cola.put(None)

def calcular(cola):
    suma_total = 0
    
    while True:
        numero = cola.get()
        if numero is None:  
            break
        suma_total += numero
    
    print(f"\nSuma total: {suma_total}")

if __name__ == "__main__":

    cola2 = multiprocessing.Queue()
    total_numeros = random.randint(1,10)

    proceso1 = multiprocessing.Process(target=generar, args=(cola2, total_numeros))
    proceso2 = multiprocessing.Process(target=calcular, args=(cola2,))

    proceso1.start()
    proceso2.start()

    proceso1.join()
    proceso2.join()
