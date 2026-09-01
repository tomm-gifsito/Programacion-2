# adaptar el programa cifrado cesar con interfaz grafica con tkinter
# Debe ingresarse un msg y un desplazamiento, y luego de apretar un boton
# Debe funcionar bien para decifrar si se usa desplazamiento negativo
# convinan conlores,opcional, usar imagenes y sonidos.Se debe entregar el codigo
# y la aplicacion .exe


import tkinter as tk
import random
from PIL import Image, ImageTk

app = tk.Tk()
app.geometry("600x400")
app.configure(background="#40807E")
tk.Wm.wm_title(app, "Cifrado César")

# --- Imagen de fondo (con PIL, quitando el blanco) ---
img = Image.open("ladrillos-removebg-preview.png").convert("RGBA").resize((600, 400))


fondo_img = ImageTk.PhotoImage(img)
fondo_label = tk.Label(app, image=fondo_img, bg="#40807E")
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
fondo_label.image = fondo_img 

des = tk.StringVar(app)
txt = tk.StringVar(app)

def cifrar(texto, desplazamiento):
    r = ""
    for ca in texto:
        if ca.isalpha():   
            if ca.isupper():
                i = ord('A')
            else:
                i = ord('a')
            nuevo_ord = (ord(ca) - i + desplazamiento) % 26 + i
            r += chr(nuevo_ord)
        else:
            r += ca
    return r

def actualizar_cifrado(event=None):
    global etiqueta_resultado
    texto_original = txt.get()
    try:
        desplazamiento = int(des.get())
    except ValueError:
        desplazamiento = 3
    texto_cifrado = cifrar(texto_original, desplazamiento)
    etiqueta_resultado.config(text=f"Texto cifrado: {texto_cifrado}")

tk.Label(
    app,
    font=("Arial",19),
    text="Cifrado Cesar",
    fg="black",
    bg="#40807E",
).pack(pady=40)

tk.Label(
    app,
    font=("Arial", 12),
    text="Escribe el texto a cifrar:",
    fg="white",
    bg="#40807E",
).pack()

entrada_texto = tk.Entry(
    app,
    font=("Comic Sans MS",20),
    textvariable=txt,
    fg="black",
    bg="grey",
    justify="center",
    width=30
)
entrada_texto.pack(pady=10)
entrada_texto.bind('<KeyRelease>', actualizar_cifrado)

tk.Label(
    app,
    font=("Arial", 12),
    text="Desplazamiento",
    fg="white",
    bg="#40807E",
).pack()

entrada_desplazamiento = tk.Entry(
    app,
    font=("Comic Sans MS",20),
    textvariable=des,
    fg="black",
    bg="grey",
    justify="center",
    width=10
)
entrada_desplazamiento.pack(pady=10)
entrada_desplazamiento.bind('<KeyRelease>', actualizar_cifrado)

etiqueta_resultado = tk.Label(
    app,
    font=("Arial", 14),
    text="txt cifrado: ",
    fg="white",
    bg="grey",
    wraplength=600
)
etiqueta_resultado.pack(pady=20)

des.set("3")
actualizar_cifrado()

app.mainloop()