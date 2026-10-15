import subprocess
import os

ruta_fichero = "alias.txt"

def main():
    print("MiniShell")
    print("Escribe 'exit' para terminar.\n")
    
    while True:
        try:
            entrada_usuario = input("> ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nSaliendo...")
            break
            
        if entrada_usuario.lower() == 'exit':
            print("Saliendo...")
            break
            
        if not entrada_usuario:
            continue

        with open(ruta_fichero, "r", encoding="utf-8") as fichero:
            if entrada_usuario in fichero.read():
                print("Encontrado")
            else:
                print(entrada_usuario)

        # try:
        #     subprocess.run(comando_final, shell=True, text=True)
        # except Exception as e:
        #     print(f"Error al ejecutar el comando: {e}")

if __name__ == "__main__":
    main()
