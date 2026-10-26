
import multiprocessing
  
def agregar_clave(diccionario, clave):
    diccionario.append(clave)
  
def print_diccionario(diccionario):
    for clave in diccionario:
        print(clave, clave[diccionario])
  
if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
  
        p1 = multiprocessing.Process(target=agregar_clave, args=(diccionario, clave))
        p2 = multiprocessing.Process(target=print_diccionario, args=(diccionario,))
  
        p1.start()
        p1.join()
  
        p2.start()
        p2.join()

