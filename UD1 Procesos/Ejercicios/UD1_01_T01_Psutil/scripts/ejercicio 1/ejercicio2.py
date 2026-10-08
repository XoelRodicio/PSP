import psutil

while True:
    print("\n--- MENÚ ---")
    print("1. Mostrar")
    print("2. Filtrar")
    print("3. Descripción")
    print("4. Salir")
    op = input("Opción: ")

    if op == "1":
        for s in psutil.win_service_iter():
            try:
                info = s.as_dict()
                print(f"{info['name']}: ({info['pid']}, {info['status']}, {info['start_type']})")
            except Exception: pass

    elif op == "2":
        traduccion = {"iniciado": "running", "parado": "stopped", "manual": "manual", "automatico": "automatic"}
        filtro = set(traduccion.get(p, p) for p in input("Filtra (ej: iniciado automatico): ").lower().split())
        
        for s in psutil.win_service_iter():
            try:
                info = s.as_dict()
                if filtro.issubset({info['status'], info['start_type']}):
                    print(f"{info['name']}: ({info['pid']}, {info['status']}, {info['start_type']})")
            except Exception: pass

    elif op == "3":
        nombre = input("Nombre del servicio: ")
        try:
            print(f"Descripción: {psutil.win_service_get(nombre).description()}")
        except Exception:
            print("Servicio no encontrado.")

    elif op == "4":
        break