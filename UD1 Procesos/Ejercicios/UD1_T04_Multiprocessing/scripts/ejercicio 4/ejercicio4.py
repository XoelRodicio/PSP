import multiprocessing

def enviar_mensaje(conexion_envio, mensaje):
    print(f"[Proceso Emisor] Enviando: '{mensaje}'")
    conexion_envio.send(mensaje)
    conexion_envio.close() 

def recibir_y_transformar(conexion_recepcion):
    """
    Función que ejecuta el segundo proceso.
    Recibe la cadena, la convierte a mayúsculas y la imprime.
    """
    mensaje_recibido = conexion_recepcion.recv()
    mensaje_mayusculas = mensaje_recibido.upper()
    print(f"[Proceso Receptor] Recibido y transformado: '{mensaje_mayusculas}'")
    conexion_recepcion.close()  

if __name__ == '__main__':

    extremo_receptor, extremo_emisor = multiprocessing.Pipe()
    
    texto_a_enviar = "Hola desde el proceso emisor usando Pipes"
    
    proceso_1 = multiprocessing.Process(target=enviar_mensaje, args=(extremo_emisor, texto_a_enviar))
    proceso_2 = multiprocessing.Process(target=recibir_y_transformar, args=(extremo_receptor,))
    
    proceso_1.start()
    proceso_2.start()
    
    proceso_1.join()
    proceso_2.join()
    
    print("Programa finalizado")
