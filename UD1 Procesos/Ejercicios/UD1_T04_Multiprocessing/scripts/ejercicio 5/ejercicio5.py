import multiprocessing

def square(numero):
    return numero*numero

if __name__ == '__main__':
    numeros = [1, 2, 3, 4, 5]

    pool = multiprocessing.Pool()

    resultados  = pool.map(square, numeros)

    print(f"Numeros orixinais: {numeros}")
    print(f"Numeros al cuadrado: {resultados}")