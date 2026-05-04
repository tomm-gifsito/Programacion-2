#Diseñar un programa que pida la fecha de nacimieno del
#usuario, e indique su edad en 2 formatos: cantidad de
#dias totales, y años-meses-dias. Mostrar en pantalla la
#fecha de nacimiento en formato Epoch/Timestamp

# investiga datetime, date.today(), datetime.now(),
# tamedelta.days

import datetime

n=0
a= datetime.date.today()
E=0
y=0
m=0
d=0
n=int(input(' porfavor ingresa tu año de nacimiento: '))
m=int(input(' porfavor ingresa tu mes de nacimiento: '))
d=int(input(' porfavor ingresa tu dia de nacimiento: '))

naci= datetime.date(n,m,d)

E= a-naci
y= E.days//365
M= E.days%365
M= M//30
D= M%30

print('usted nació en: ',naci)
print('usted tiene ',E.days,' dias de vida')

print('y usted tiene ',y,' años usted tiene ',M,' meses y ',D,' dias')



