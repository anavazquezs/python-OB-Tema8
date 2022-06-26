# f = open("archivoTexto.txt", "x")

#f = open("archivoTexto.txt", "w")

#f.writelines("TITULO: Ejemplo de manejo de archivos en Python\n", "Este es el primer parrafo.\n", "Este es el segundo parrafo.\n", "Este es el ultimo parrafo.\n")

f = open("archivoTexto.txt", "r")
print(f.read())

f.close()
