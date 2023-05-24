def sumcol(A1, y): #defino una funcion conn las variables respectivas
    s = 0 #hago un contador
    for x in A1:
        s += x[y] #sumo los elemento de la columna
    return s

A1=[] # hago un arreglo
a1 = int(input("Ingrese el número de filas para la matriz: "))
a2 = int(input("Ingrese el número de columnas para la matriz: ")) 
for i in range(a1):
    fila = [] # hago un arreglo
    for j in range(a2):
        x = int(input(f"Ingrese el valor para la posición ({i+1}, {j+1}): "))
        fila.append(x)
    A1.append(fila) #mismo proceso para hacer una matriz

y = int(input("ingrese el numero de la columna menos 1: ")) #pido el numero de columna

print(sumcol(A1,y)) # imprimo los resultados