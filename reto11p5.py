def sumfila(A1, x): #defino una funcion conn las variables respectivas
    s = 0 #hago un contador 
    for j in A1[x]: # sumo la fila dada
        s += j
    return s

A1 = [] # hago un arreglo
a1 = int(input("Ingrese el número de filas para la matriz: "))
a2 = int(input("Ingrese el número de columnas para la matriz: "))
for i in range(a1):
    fila = [] # hago un arreglo
    for j in range(a2):
        x = int(input(f"Ingrese el valor para la posición ({i+1}, {j+1}): "))
        fila.append(x)
    A1.append(fila) # hago la matriz de la misma forma

x= int(input("Ingrese el número de la fila menos 1: ")) #pido el numero de la fila

print(sumfila(A1, x)) #imprimo la suma