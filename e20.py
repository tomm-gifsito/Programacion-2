# adaptar el programa cifrado cesar con interfaz grafica con tkinter
# Debe ingresarse un msg y un desplazamiento, y luego de apretar un boton
# Debe funcionar bien para decifrar si se usa desplazamiento negativo
# convinan conlores,opcional, usar imagenes y sonidos.Se debe entregar el codigo
# y la aplicacion .exe


import tkinter as tk #llamamos a la libreria
import random


# creamos una variable de clase tkinter
app = tk.Tk()

# escribimos las DIMENCIONES de el "lienzo"
# ancho y alto
app.geometry("600x400")

# app.configure(backgrund= el color q quieras de fondo )
app.configure(background="#40807E")

# cambiara el nombre de la pestaña a con un titulo principal
tk.Wm.wm_title(app, "decifrado cesar")

des= tk.StringVar(app)
txt = tk.StringVar(app)

def cifrar(text, des):
    R = ""
    
    for Ca in M:

        if Ca.isalpha():   

            if Ca.isupper():
                i = ord('A')
            else:
                i = ord('a')
                
# formula:--- nuevo_ord = (ord(CAracter)(el numerin en ASCII) - Inicio(97) + Desplazamiento(se mueve de un numero al otro)) % 26(va por el abecedario) + inicio(traducimos de ASCII a caracter)---

            nuevo_ord = (ord(Ca) - i + D) % 26 + i
            R += chr(nuevo_ord)
        else:
            R += Ca
    
    return R

#etiketa(titulo)
tk.Label(
    app,
    font=("Arial",19),
    text="Cifrado Cesar",
    fg="black",
    bg="blue",
).pack(pady=40)

#etiketa(numero de desplazamiento)
tk.Entry(
    app,
    font=("Comic Sans MS",20),
    textvariable= des,
    fg="black",
    bg="grey",
    justify="center",
).pack(pady=60)


#etiketa(cifrado)
tk.Label(
    app,
    font=("Arial", 14),
    textvariable=R,
    fg="white",
    bg="#002147",
).pack(pady=15)

#escribe el texto a decifrar
tk.Entry(
    app,
    font=("Comic Sans MS",20),
    textvariable= txt,
    fg="black",
    bg="grey",
    justify="center",
).pack(pady=60)
entrada.bind('<KeyRelease>', actualizar_cifrado)