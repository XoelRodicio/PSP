import multiprocessing

def enviarCadena(conn, msg):
    conn.send(msg)
    conn.close()

def convertirMaiusculas(conn):
    texto = conn.recv()
    texto = texto.upper()
    conn.close()

    print(f"Texto  recivido: {texto}")


if __name__ == '__main__':
    msg = input("Escribe un mensaje:")
    conn1, conn2 = multiprocessing.Pipe()

    p1 = multiprocessing.Process(target=enviarCadena, args=(conn1, msg))
    p2 = multiprocessing.Process(target=convertirMaiusculas, args=(conn2, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()