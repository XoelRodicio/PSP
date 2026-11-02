import multiprocessing

def calcular_cuadrado(numero):
    return numero ** 2

if __name__ == '__main__':
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print(f"[Proceso Principal] Lista original: {numeros}")
    
    with multiprocessing.Pool() as pool:

        resultados = pool.map(calcular_cuadrado, numeros)
    
    print(f"Resultados (cuadrados): {resultados}")

