vidas=6
perder=1
vidas=5
num=0
numsecret=0
import random
numsecret=random.randint(1,20)
print('BIENVENIDO A LA ADIVINANZA, EL JUEGO CONSISTE EN ADIVINAR UN NUMERO DEL 1-20')
num=int(input('QUE EMPIEZE EL JUEGO: '))
while(vidas!=0):  
    if (numsecret==num):
            print('Felicidades ganaste el juego')
            break
    else:
        if (numsecret>num):
            vidas=vidas-perder
            print('ERROR te quedan',vidas,'vidas')
            num=int(input('el NUMERO SECRETO es mas alto:  '))
        
        else:
            vidas=vidas-perder
            print('ERROR te quedan',vidas,'vidas')
            num=int(input('el NUMERO SECRETO es mas bajo:  '))    
if(vidas==0):
    print('PERDISTE TODAS LAS VIDAS')

