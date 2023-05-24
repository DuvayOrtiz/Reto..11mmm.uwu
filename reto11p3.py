def trans(A1): #defino una funcion conn las variables respectivas
    f = len(A1)
    c = len(A1[0]) #longitud de filas y columnas
    lavainaesa = [] # hago un arreglo
    for j in range(c):
        f2 = [] # hago un arreglo
        for i in range(f):
            f2.append(A1[i][j])
        lavainaesa.append(f2)
    return lavainaesa #se hace otro arreglo con la matrices transpuesta
A1=[] # hago un arreglo
a1 = int(input("Ingrese el número de filas para la matriz: "))
a2 = int(input("Ingrese el número de columnas para la matriz: ")) # numero de filas y columnas
for i in range(a1):
    fila = [] # hago un arreglo
    for j in range(a2):
        x = int(input(f"Ingrese el valor para la posición ({i+1}, {j+1}): "))
        fila.append(x)
    A1.append(fila) # pido elementos
print(trans(A1)) #imprimo la transpuesta