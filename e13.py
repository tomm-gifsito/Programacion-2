#Implementar en Python una función para aplicar cifrado cesar a una
#cadena se debe pasar el mensaje y el desplazamiento como parámetros.La
#misma funcion debe descifrar el mensaje si se aplica un desplazamiento negativo
 
 ## ord=ordinal de un caracter(numero del caracter)
 ## chr=caracter del numero

M=input('ingrese el numero que sera cifrado en cifrado cesar :')
D=int(input('ingrese el desplazamiento :'))

def Cc(M, D):
    R = ""
    
    for Ca in M:
#         .isalpha() se asegura que sea cadena de SOLO texto
        if Ca.isalpha():   
#             .isupper() verifica las mayusculas
            if Ca.isupper():
                i = ord('A')
            else:
                i = ord('a')
                
# formula: ---nuevo_ord = (ord(caracter)(el numerin en ASCII) - inicio(97) + desplazamiento(se mueve de un numero al otro)) % 26(va por el abecedario) + inicio(traducimos de ASCII a caracter)---

            nuevo_ord = (ord(Ca) - i + D) % 26 + i
            R += chr(nuevo_ord)
        else:
            R += Ca
    
    return R


Mc= Cc(M, D)
print(f'Mensaje cifrado: {Mc}')

Md = Cc(Mc, -D)
print(f'Mensaje descifrado: {Md}')
    