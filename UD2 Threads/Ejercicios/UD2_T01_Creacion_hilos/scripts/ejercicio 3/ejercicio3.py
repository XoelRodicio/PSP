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
            try:
                print(f"PID: {p.info['pid']} || NOMBRE: {p.info['name']} || USERNAME: {p.info['username']}" )
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
                
    elif opcion == "2":
        print("\nFILTRAR POR USO DE MEMORIA")
        porcentaje = float(input("Introduce el % de memoria mínimo: "))
        
        procesos = [p for p in psutil.process_iter(attrs=['pid', 'name', 'username']) if p.memory_percent() > porcentaje]
        procesos.sort(key=lambda p: p.memory_percent(), reverse=True)
        
        for p in procesos:
            print(f"PID: {p.info['pid']} || NOMBRE: {p.info['name']} || MEMORIA: {p.memory_percent():.2f}%")

    elif opcion == "3":
        print("\nFILTRAR POR USO DE CPU")
        porcentaje_cpu = float(input("Introduce el % de CPU mínimo: "))
        
        procesos_validos = []
        for p in psutil.process_iter(attrs=['pid', 'name', 'username', 'memory_info']):
            try:
                uso_cpu = p.cpu_percent(interval=0.5)
                if uso_cpu > porcentaje_cpu:
                    procesos_validos.append((p, uso_cpu))
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
                
        procesos_validos.sort(key=lambda x: x[1])
        
        for p, cpu in procesos_validos:
            print(f"PID: {p.info['pid']} || NOMBRE: {p.info['name']} || CPU: {cpu:.2f}%")

    elif opcion == "4":
        print("\nARBOL DE PROCESOS")
        print(f"(Para probar, el PID de este programa actual es: {psutil.Process().pid})")

        pid_usuario = int(input("Introduce un PID para ver su árbol: "))
        
        if not psutil.pid_exists(pid_usuario):
            print("El proceso no existe.")
        else:
            def pintar_arbol(pid, nivel=0):
                try:
                    p = psutil.Process(pid)
                    espacios = "  " * nivel
                    sep = espacios + u'\u2514'+u'\u2500'+u'\u2500 ' if nivel > 0 else ""
                    
                    print(f"{sep}PID: {pid}, Nombre: {p.name()}")
                    for h in p.children():
                        pintar_arbol(h.pid, nivel + 1)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass

            pintar_arbol(pid_usuario)
            
    elif opcion == "5":
        print("Bye ye")
        break
