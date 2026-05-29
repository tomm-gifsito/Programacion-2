#Declarar una matriz de 4 filas y 4 columnas con números enteros sucesuvos a partir del 1 en cada celda
#calcula la suma y la multiplicacion de la contra diagonal. Mostrar en pantalla estos valores y los elementos
#de la matriz

M=[[1,2,3,4],
   [5,6,7,8],
   [9,10,11,12],
   [13,14,15,16],]

for fila in M:
    print(fila)

f= 4
suma = 0
multi = 1
diagonal = []

for i in range(f):
    for j in range(f):
        if i + j == f - 1:
            elemento = M[i][j]
            diagonal.append(elemento)
            suma+= elemento
            multi*= elemento
            
print('Elementos diagonal: ',diagonal)
print('Suma diagonal: ',suma)
print('Multiplicación diagonal: ',multi)