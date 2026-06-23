#importar en python una imagen y almacenarla en una matriz. Implementar una funcion para rotar la imagen. preguntar si quiere rotar
#90 grados a la izquierda o a la derecha o 180 grados. Mostrar la imagen original y la rotada
##no usar funciones ya establecidas

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

usuario=int(input("quiere rotar la imagen 90 grados hacia \n la derecha(1)\n la izquierda(2)\n180 grados?(3) \n"))

foto = Image.open('floramarilla.jpg').convert("L")
foto = np.array(foto)
dimen= np.shape(foto)

fil=dimen[0]
colum=dimen[1]

def derecha1(image_input):
    fil, colum = image_input.shape
    
    rotada = np.zeros((colum, fil), dtype=image_input.dtype)
    
    for i in range(fil):
        for j in range(colum):
            rotada[j][fil - 1 - i] = image_input[i][j]
    return rotada

def izquierda2(image_input):
    fil, colum = image_input.shape
    
    rotada = np.zeros((colum, fil), dtype=image_input.dtype)
    
    for i in range(fil):
        for j in range(colum):
            rotada[colum - 1 - j][i] = image_input[i][j]
    return rotada

def vuelta3(image_input):
    a=derecha1(image_input)
    b=derecha1(a)
    return b

    

if (usuario==1):
    plt.subplot(1,2,1)
    plt.imshow(foto, cmap="grey")
    plt.title('original')
    plt.subplot(1,2,2)
    plt.title('rotado hacia la derecha')
    plt.imshow(derecha1(foto), cmap='gray')
    plt.show()
    
elif (usuario==2):
    rizq = izquierda2(foto)
    plt.subplot(1,2,1)
    plt.imshow(foto, cmap="grey")
    plt.title('original')
    plt.subplot(1,2,2)
    plt.title('rotado hacia la izquierda')
    plt.imshow(rizq, cmap='gray')
    plt.show()
    
else:
    rv = vuelta3(foto)
    plt.subplot(1,2,1)
    plt.imshow(foto, cmap="grey")
    plt.title('original')
    plt.subplot(1,2,2)
    plt.imshow(rv, cmap='gray')
    plt.title('rotado 180 grados')
    plt.show()
