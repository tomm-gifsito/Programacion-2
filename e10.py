#Escribir una funcion para convertir temperatura de celsius a Fahrenheit y
#otra funcion para la conversion opuesta

P=int(input('convertir \nFahrenheit a celcius(1) \ncelcius a Fahrenheit(2):  '))


def F_A_C(F):
    Cel = (F - 32) * 5/9 #( °F − 32) × 5/9 formula  (gracias google) 
    return Cel
def C_A_F(C):
    Fa = (C * 9/5) + 32  #( °C × 9/5) + 32
    return Fa


if P==1:
    F=int(input('ingrese la temperatura:  '))
    print(F_A_C(F))
else:
    C=int(input('ingrese los celcius:  '))
    print(C_A_F(C))
      