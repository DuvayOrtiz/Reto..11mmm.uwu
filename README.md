# Reto..11mmm.uwu
## :star: Haciendo el reto 11 :sparkles:
![image](https://github.com/DuvayOrtiz/reto10uwu/assets/124726079/9776a211-9b59-4267-be4e-13d330bef310)
![image](https://github.com/DuvayOrtiz/reto10uwu/assets/124726079/6a0c7207-88f8-406d-b220-41dfbe4ecb42)
## :star: Sigo esperando que cree el canal :D :dizzy:
## :star: punto 1 :zap:
```ruby
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

```
## :star: Punto 2 :boom:
```ruby
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
```
## :star: Punto 3 :collision:

```ruby
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
```

## :star: Punto 4 :sunny:

```ruby
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
```
## :star: Punto 5 :high_brightness:

```ruby
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
```
