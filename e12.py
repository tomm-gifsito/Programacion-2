#Los estudiantes deben pasar al frente a exponer, pero nadie quiere pasar primero
#diseñar un programa con una lista con los nombres de los estudiantes, y de forma
#aleatoria generar otra lista que indique el orden en el que deben pasar a exponer
##bucle for in range(len(estudiantes)):
##Para añadir un elemento a una lista se puede usar el metodo append()
import random

estudi=[]

e1=str(input('ingrese el primer estudiante: '))
e2=str(input('ingrese el segundo estudiante: '))
e3=str(input('ingrese el tercer estudiante: '))
e4=str(input('ingrese el cuarto estudiante: '))

estudi.append(e1)
estudi.append(e2)
estudi.append(e3)
estudi.append(e4)

print(estudi)

#random.sample desordena la lista
orden=random.sample(estudi, len(estudi))

print(orden)


