import tkinter as tk #llamamos a la libreria
import random


# creamos una variable de clase tkinter
app = tk.Tk()

vidas=6
numsecret=0

numsecret=random.randint(1,20)
resultado = tk.StringVar(app)
vidassv = tk.StringVar(app)
entrada = tk.StringVar(app)

vidassv.set("Vidas: 6")

def intento():
    global vidas
    print("numeros: "+entrada.get())
    num=int(entrada.get())
    vidas =vidas - 1
    vidassv.set("Vidas: " + str(vidas))
    
    if (numsecret==num):
        resultado.set('Felicidades ganaste el juego')
        return
    elif(numsecret>num):

        resultado.set("ERROR el NUMERO SECRETO es mas alto")
        
    else:
        resultado.set("ERROR el NUMERO SECRETO es mas bajo")
        
    if(vidas<=0):
        resultado.set("PERDISTE, el número era: " + str(numsecret))
        entrada.set("")
        bt_adivina.config(state="disabled")

# escribimos las DIMENCIONES de el "lienzo"
# ancho y alto
app.geometry("400x600")

# app.config(backgrund= el color q quieras de fondo )
app.configure(background="#002147")

# cambiara el nombre de la pestaña a con un titulo principal
tk.Wm.wm_title(app, "ADIVINA EL NUMERO")


#etiketa(titulo)
tk.Label(
    app,
    font=("Arial",19),
    text="ADIVINA EL NUMERO DEL 1-20",
    fg="black",
    bg="blue",
).pack(pady=40)

#etiketa(vidas)
tk.Label(
    app,
    font=("Arial",19),
    textvariable= vidassv,
    fg="black",
    bg="blue",
).pack(pady=20)

#etiketa(resul)
tk.Label(
    app,
    font=("Arial", 14),
    textvariable=resultado,
    fg="white",
    bg="#002147",
).pack(pady=15)

#entrada d text
tk.Entry(
    app,
    font=("Comic Sans MS",20),
    textvariable=entrada,
    fg="black",
    bg="grey",
    justify="center",
).pack(pady=60)

#boton
canvas = tk.Canvas(
    app,
    width=150,
    height=150,
    bg="#002147",
    highlightthickness=0
)
canvas.pack(pady=10)

boton_redondo = canvas.create_oval(
    10, 10, 140, 140,
    fill="#FF6B35",
    outline="#CC5533",
    width=3
)

# Texto del botón
texto_boton = canvas.create_text(
    75, 75,
    text="ADIVINAR",
    font=("Arial", 14, "bold"),
    fill="white"
)

# Efectos hover
def on_enter(e):
    canvas.itemconfig(boton_redondo, fill="#FF8A5C")
    
def on_leave(e):
    canvas.itemconfig(boton_redondo, fill="#FF6B35")

# Eventos del botón
canvas.tag_bind(boton_redondo, "<Button-1>", lambda e: intento())
canvas.tag_bind(texto_boton, "<Button-1>", lambda e: intento())
canvas.tag_bind(boton_redondo, "<Enter>", on_enter)
canvas.tag_bind(boton_redondo, "<Leave>", on_leave)


app.mainloop()