#Hacer una aplicacion co n GUI tkinter para cifrar mensajes con cifrado Vigenere. Debe funcionar con mensajes con "ñ".Generar el .exe

import tkinter as tk

app = tk.Tk()

# ancho y alto
app.geometry("600x400")

# app.config(backgrund= el color q quieras de fondo )
app.configure(background="#b0323d")

# cambiara el nombre de la pestaña a con un titulo principal
tk.Wm.wm_title(app, "Cifrado Vigenere")

abc=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z]

tk.Label(
    app,
    font=("Arial",19),
    text="gasb",
    fg="black",
    bg="#b0323d",
).pack(pady=40)

#entrada d text
tk.Entry(
    app,
    font=("Comic Sans MS",20),
    textvariable=entrada,
    fg="black",
    bg="grey",
    justify="center",
).pack(pady=60)