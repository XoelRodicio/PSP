import psutil

while True:
    print("\n--- MENÚ ---")
    print("1. Mostrar informacion")
    print("2. Filtrar por uso de memoria")
    print("3. Filtrar por uso de CPU")
    print("4. Mostar arbol de procesos")
    print("5. Salir")
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        print("\nMOSTRAR INFORMACION DE TODOS LOS PROCESOS")
        procesos = [p for p in psutil.process_iter(attrs=['pid', 'name', 'username'])]

        for p in procesos:
            print(f"PID: {p.info['pid']} || NOMBRE: {p.info['name']} || USERNAME: {p.info['username']}" )
    elif opcion == "2":
        print("\nFILTRAR POR PROCESOS DE MEMORIA")
    elif opcion == "3":
        print("Hola3")
    elif opcion == "4":
        print("Hola4")
    elif opcion == "5":
        print("Bye ye")
        break