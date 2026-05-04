#un cajeero automatico entrega solo billetes de $1000 y de de $200. Ingresa
#la cantidad que desea extraer el usuario, y luego indicar cuantos billetes de
#100 y de 200 se le entregan. indicar ademas el saldo que no se pudo extraer
#porque no hay billetes

plata=int(input('cuanto extraes  '))
bille1= plata//1000
bille2= (plata%1000)//200
noplata=((plata%1000)%200)
print('billetes de 1000: ',bille1,'\nbilletes de 200: ',bille2,'\nsaldo acabado: ',noplata)



