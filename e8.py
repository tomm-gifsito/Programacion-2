#Escribir una funcion que calcule el area de un circulo, Luego escribir una funcion que calcule
#el volumen de un cilindro llamando a la primera funcion

import math

V=0
A=0
ancho=0
alto=0

ancho=int(input('cuanto de ancho tiene el cilindro?:  '))
alto=int(input('cuanto de alto tiene el cilindro?:  '))

def A(ancho):
    A = math.pi * ancho**2  # A=π×r  forma de sacar el area (odio matematica)
    return A

def V(ancho, alto):
    V = A(ancho)
    V = V * alto
    return V

ancho= ancho/2  #Divide el circulo a la mitad

print('el area de circulo es :',A(ancho))
print('el volumen de circulo es :',V(ancho, alto))

