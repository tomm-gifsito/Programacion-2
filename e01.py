edad=0
añodnacimiento=0
añoacual=0
nombre=''
print('Hola, ingrese su nombre: ')
nombre=input()
print('Hola,',nombre,'ingresa tu fecha de nacimiento: ')
añodnacimiento=int(input())
añoactual=int(input('ingresa la fecha del año actual: '))
edad= añoactual - añodnacimiento
print('Gracias por registrarte!! su usuario es: ',nombre,' y su edad ',edad)