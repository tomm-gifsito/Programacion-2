# Importar en python una imagen a color y mostrarla. Definir una funcion para convertir imagenes en escala de grises
# y mostrar el resultado. No usar funciones integradas, en su lugar usar la formula .convert('L') para pasarlo a grises
# # grises= R*0.2989 + G*0.5870 + B*0.1140

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


foto = Image.open('/content/sample_data/floramarilla.jpg')
foto = np.array(foto)
dimen= np.shape(foto)

def convertir(image_input):
    alto = image_input.shape[0]
    ancho = image_input.shape[1]

    grises = np.zeros((alto, ancho), dtype=np.uint8)

    # Recorrer cada píxel
    for i in range(alto):
        for j in range(ancho):
            # para obtener el rgb de los pixeles
            R = image_input[i, j, 0]
            G = image_input[i, j, 1]
            B = image_input[i, j, 2]

            # formula
            val = int(R * 0.2989 + G * 0.5870 + B * 0.1140)
            grises[i, j] = max(0, min(255, val))

    return grises


gris_converted = convertir(foto)

plt.imshow(foto)
plt.show()
plt.imshow(gris_converted, cmap='gray')
plt.show()
