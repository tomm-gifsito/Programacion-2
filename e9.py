#Escribir una funcion donde el usuario ingresa un numero entero positivo
#(validarlo) y calcular el factorial

n=int(input('ingresa un numero positivo porfis:  '))

def factorial(n):
    if n<0:
        raise print('error!!! ingresaste un numero negativo')
    
    else:
        R=1 #necesita ser 1 numero
        for x in range(2, n + 1):#saca los numeros anteriores
            R = R *x #acumula y multiplica
        return R

print(factorial(n))