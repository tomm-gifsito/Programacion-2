#conversor DECIMAL-BINARIO-HEXADECIMAL diseñar un programa que el usuario ingresa un numero y desde que sistema hacia que
#sistema de enumeracion. Ademas mostarr el caracter ASCII que corresponde al numero

num=0
hexa=0
bina=0
deci=0
SIS=0

print('conversor decimal,binario,hexadecimal')

SIS=int(input('elige el a cual sistema numerico que va a ingresar \nBinario(1)  \nHexadecimal(2) \nDecimal(3):  '))
if SIS == 1:
    num=int(input('ingresa el numero en binario:  '))
elif SIS == 2:
    num=(input('ingresa el numero en hexa:  '))
elif SIS == 3:
    num=int(input('ingresa el numero en decimal:  '))
else:
    print('❌ opción no válida, elija 1, 2 o 3')
S=int(input('elige el a cual sistema numerico pasar \nBinario(1)  \nHexadecimal(2)  \nDecimal(3):  '))

if S == 1:
    R = bin(num)
    print(R)
elif S == 2:
    R = hex(num)
    print(R)
elif S == 3:
    R = int(num, 16)
    print(R)
else:
    print('❌ opción no válida, elija 1, 2 o 3')