#un profe tiene X caramelos y quiere repartir entre Y estudiantes reciben un
#numero entero de caramelos.Preguntar al usuario X e Y. Luego indicar cuantos
#caramelos le tocan a cada estudiante y cuantos sobran en la bolsa

caramelos=int(input('cuantos caramelos tiene el profe?:  '))
estu=int(input('cuantos estudiantes hay:  '))
divicion= caramelos//estu
sobra= caramelos%estu
print('a cada estudiate se le dan ',divicion,' caramelos y sobran ',sobra)