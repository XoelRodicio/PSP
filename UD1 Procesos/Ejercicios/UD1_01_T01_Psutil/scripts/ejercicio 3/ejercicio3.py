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
        print("\nFILTRAR POR USO DE MEMORIA")
        procesos = [p for p in psutil.process_iter(attrs=['pid', 'name', 'username']) if p.memory_percent()>1]
        procesos.sort(key=lambda p: p.memory_percent(), reverse=True)
        print(procesos)

    elif opcion == "3":
        print("\nFILTRAR POR USO DE CPU")
        procesos = [p for p in psutil.process_iter(attrs=['pid', 'name', 'username','memory_info']) if p.cpu_percent(interval=0.1)>0.001]
        procesos.sort(key=lambda p: p.cpu_percent(interval=0.1))
        print(procesos)

    elif opcion == "4":
        print("\nARBOL DE PROCESOS")
        def pintar_arbol(pid, sep=u'\u2514'+u'\u2500'+u'\u2500'):
            p = psutil.Process(pid)
            print(f"{sep}PID: {pid}, Nombre: {p.name()}")
            for h in p.children():
                pintar_arbol(h.pid, "|  "+sep)
    elif opcion == "5":
        print("Bye ye")
        break