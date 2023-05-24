def multi(A1, A2): #defino una funcion conn las variables respectivas
    S1 = [] # hago un arreglo vacio
    for i in range(len(A1)):
        S2 = [] # hago un arreglo vacio
        for j in range(len(A2[0])): 
            sumaA1A2 = 0
            for k in range(len(A1[0])):
                sumaA1A2 += A1[i][k] * A2[k][j]
            S2.append(sumaA1A2)
        S1.append(S2)
    return S1 # hago lo mismo de la suma y resta pero con multipliacion

a1 = int(input("Ingrese el número de filas para la matriz A1: "))
a2 = int(input("Ingrese el número de columnas para la matriz A1: "))
a3= int(input("Ingrese el número de filas para la matriz A2: "))
a4 = int(input("Ingrese el número de columnas para la matriz A2: ")) #pido numero de filas y columnas

A1 = [] # hago un arreglo
A2 = [] # hago un arreglo

print("Ingrese los valores para la matriz A1:")
for i in range(a1):
    fila = [] # hago un arreglo
    for j in range(a2):
        x = int(input(f"Ingrese el valor para la posición ({i+1}, {j+1}): "))
        fila.append(x)
    A1.append(fila)

print("Ingrese los valores para la matriz A2:")
for i in range(a3):
    fila = [] # hago un arreglo
    for j in range(a4):
        x = int(input(f"Ingrese el valor para la posición ({i+1}, {j+1}): "))
        fila.append(x)
    A2.append(fila)
    # pido los elementos de la matriz
if a1==a3 and a2==a4:
    print("El producto de las matrices es:", multi(A1, A2))
else:
    print("no miden lo mismo") # comparo las matrices y doy el resultado