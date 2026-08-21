# aplicar un filtro de desenfoque Gaussiano a una imagen. Mostrar la imagen original y la filtrada. Hacer la
# convolution manual desde la celda (1,1) hasta la (n-1,n-1). Usar el Kernel.

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

foto = Image.open('floramarilla.jpg')
foto = np.array(foto)
dimen = np.shape(foto)
        
kernel = np.array([
    [1/16, 2/16, 1/16],
    [2/16, 4/16, 2/16],
    [1/16, 2/16, 1/16]
])

# Determinar si la imagen es a color o en escala de grises
if len(dimen) == 3:
    fil, colum, canales = dimen
    es_color = True
else:
    fil, colum = dimen
    canales = 1
    es_color = False
    foto = foto.reshape(fil, colum, 1)

# Crear una copia de la imagen original para la imagen filtrada
foto_filtrada = np.zeros_like(foto, dtype=np.float64)

# Aplicar el filtro 
for i in range(1, fil - 1):
    for j in range(1, colum - 1):
        for c in range(canales):
            ventana = foto[i-1:i+2, j-1:j+2, c]
            valor_filtrado = np.sum(ventana * kernel)
            foto_filtrada[i, j, c] = valor_filtrado


foto_filtrada = foto_filtrada.astype(np.uint8)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(foto)
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(1, 2, 2)
if es_color:
    plt.imshow(foto_filtrada)
else:
    plt.imshow(foto_filtrada[:, :, 0], cmap='gray')
plt.title('Imagen con Filtro Gaussiano')
plt.axis('off')

plt.tight_layout()
plt.show()