import random
def llenarVector(arreglo):
    for i in range (10):
        r=random.randint(1,100)
        arreglo.append(i)
    return arreglo
def Promedio (arreglo):
    sumatorio=0
    for valor in arreglo:
        sumatorio+=valor
    sumatorio=sumatorio/len(arreglo)
    return sumatorio
def ParesImpares(arreglo):
    sumapar=0
    sumaimpar=0
    for i in range(len(arreglo)):
        if i%2==0:
            sumapar+=arreglo[i]
        else:
            sumaimpar+=arreglo[i]
    print("La suma par es ", sumapar)
    print("La suma impar es ", sumaimpar)
#Ejercicio2
def ContarParImpar(matriz):
    par=0
    impar=0
    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]%2==0:
                par+=1
            else:
                impar+=1
    print("La cantidad de numeros pares es", par )
    print("La cantidad de numeros impares es", impar )

print("Semana No.16: Ejercicio 1")
vector=[]
vector=llenarVector(vector)
print(vector)
print("El promedio es: ", Promedio(vector))
print("Longitud de del arreglo:", len(vector))
ParesImpares(vector)
print("∖ Semana 16: ejercicio 2 ")

filas=int(input("Ingrese la cantidad de filas:"))
columnas=int(input("Ingrese la cantidad de columnas:"))
matriz=[]
for i in range(filas):
    for j in range (columnas):
        temp=[]
        r=random.randint(0,1001)
        temp.append(temp)
    matriz.append(matriz)
print(matriz)
ContarParImpar(matriz)