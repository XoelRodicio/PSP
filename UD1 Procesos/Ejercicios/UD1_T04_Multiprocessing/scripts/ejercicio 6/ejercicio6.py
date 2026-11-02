import multiprocessing

def incrementar(contador, lock):
    for _ in range(100):
        lock.acquire()

        contador.value = contador.value + 1

        lock.release()

if __name__ == '__main__':
    contador = multiprocessing.Value('i',0)
    lock = multiprocessing.Lock()

    proceso1 = multiprocessing.Process(target=incrementar, args=(contador, lock))
    proceso2 = multiprocessing.Process(target=incrementar, args=(contador, lock))

    proceso1.start()
    proceso2.start()

    proceso1.join()
    proceso2.join()

    print(f"Valor final del contador: {contador.value}")