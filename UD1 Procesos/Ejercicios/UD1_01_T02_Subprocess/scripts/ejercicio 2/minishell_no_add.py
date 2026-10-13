
fichero = "alias.txt"
alias = {}
with open(fichero, "r") as fichero:
    alias = { k:v for k,v in list(map(lambda linea: linea.strip("\n").split("="),fichero.readlines()))}

# for linea in fichero.readline():
# # separar la linea en dos partes y meter en el diccionario clave = valor
# k,v = linea.strip("\n").split("=")
# alias[k]=v
# meter cosas en diccionario alias

print(alias)