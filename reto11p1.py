def sumita(A1, A2): #defino una funcion con las variables respectivas
    S1 = [] # hago un arreglo
    for i in range(len(A1)):  #recorrer el arreglo
        S2 = []  # hago un arreglo
        for j in range(len(1[0])): #recorro la matriz
            sumaA1A2 = A1[i][j] + A2[i][j]  #sumo los componentes de la misma
            S2.append(sumaA1A2)  # la agrego a otra matriz
        S1.append(S2)      
    return S1
# hago lo mismo pero con la resta :D
def restita(A1, A2): 
    S1 = []
    for i in range(len(A1)): 
        S2 = [] 
        for j in range(len(A1[0])): 
            sumaA1A2 = A1[i][j] - A2[i][j] 
            S2.append(sumaA1A2) 
        S1.append(S2)      
    return S1
a1 = int(input("Ingrese el número de filas: "))
a2 = int(input("Ingrese el número de columnas: ")) # pedimos el numero de columnas y filas

A1=[]
A2=[] #creamos dos arreglos vacios
for i in range(a1):
    fila = []
    for j in range(a2):
        x = int(input(f"Ingrese el valor para la posición ({i+1}, {j+1}): "))
        fila.append(x)
    A1.append(fila) #pedimos los elementos de la raiz
for i in range(a1):
    fila = []
    for j in range(a2):
        x = int(input(f"Ingrese el valor para la posición ({i+1}, {j+1}): "))
        fila.append(x)
    A1.append(fila) 
    
x = int(input("ingrese 1 si desea suma y 2 si quiere resta: ")) #pedimos una de las funciones

if x==1:
    print(sumita(A1,A2)) #condiciono la función y la imprimo
elif x==2:
    print(restita(A1,A2))
else:
    print("no está en las opciones")#en caso de no ser ninguna funcion se imprime el error 