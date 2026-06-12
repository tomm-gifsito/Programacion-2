#Importar en python una imagen en escala de grises y almacenarla en una matriz.Mostrar la imagen en pantalla.
#Luego ordenar los valores numericos para volotear la imagen horizontalmente y mostrar el valor en pantalla
## numpy, matplotlib, pillow


from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


foto = Image.open('floramarilla.jpg').convert('L')
foto = np.array(foto) # Convierte PIL a NumPy array

plt.imshow(foto, cmap='grey')
plt.show()
for i in range(len(foto)):

    for j in range(len(foto[0])//2): # "//2" solo recorre la mitad(porque sino como son 4 vueltas lo solucionara y volvera otra vez al estado original)

        aux=foto[i][j] # guardamos el primer numero (0x0)

        idop=len(foto[0])-1-j # guardamos el ultimo numero

        foto[i][j]=foto[i][idop] # lo colocamos como primero
        foto[i][idop]=aux
plt.imshow(foto, cmap='grey')
plt.show()
        