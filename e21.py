# Conversor de unidades con tkinter (como el conversor de Google)
# OptionMenu para la categoría, Combobox para la conversión y dos Entry:
# al escribir en uno se actualiza el otro.
#
# A) Longitud: M a KM; M a Millas; CM a Pulgadas; M a Pies
# B) Temperatura: Celsius a Fahrenheit; Celsius a Kelvin; Fahrenheit a Kelvin
# C) Masa: KG a LB; Gramos a Onzas; Tn a KG
# D) Velocidad: Km/h a Mph; Km/h a m/s; Km/h a Nudos
# E) Volumen: Litros a Galones; Litros a Pies cúbicos
# F) Monedas: Pesos a Dólares; Pesos a Reales; Pesos a Euros
# G) Informática: B - KB - MB - GB - TB

import tkinter as tk
from tkinter import ttk

FONDO = "#038554"   # fondo de la ventana
COLOR = "#025032"   # desplegables y título
CLARO = "#047049"   # opción seleccionada

# Cuántos PESOS vale 1 unidad (valores de ejemplo, actualizalos)
PESOS_POR_USD = 1400
PESOS_POR_BRL = 260
PESOS_POR_EUR = 1600


def lineal(f):
    """Devuelve (ida, vuelta) para una conversión de multiplicar por f."""
    return (lambda x: x * f, lambda y: y / f)


# Cada conversión es un par: (origen -> destino, destino -> origen)
CONVERSIONES = {
    "Longitud": {
        "M a KM": lineal(1 / 1000),
        "M a Millas": lineal(1 / 1609.344),
        "CM a Pulgadas": lineal(1 / 2.54),
        "M a Pies": lineal(3.28084),
    },
    "Temperatura": {
        "Celsius a Fahrenheit": (lambda x: x * 9 / 5 + 32,
                                 lambda y: (y - 32) * 5 / 9),
        "Celsius a Kelvin": (lambda x: x + 273.15,
                             lambda y: y - 273.15),
        "Fahrenheit a Kelvin": (lambda x: (x - 32) * 5 / 9 + 273.15,
                                lambda y: (y - 273.15) * 9 / 5 + 32),
    },
    "Masa": {
        "KG a LB": lineal(2.20462),
        "Gramos a Onzas": lineal(1 / 28.3495),
        "Tn a KG": lineal(1000),
    },
    "Velocidad": {
        "Km/h a Mph": lineal(1 / 1.609344),
        "Km/h a m/s": lineal(1 / 3.6),
        "Km/h a Nudos": lineal(1 / 1.852),
    },
    "Volumen": {
        "Litros a Galones": lineal(1 / 3.78541),
        "Litros a Pies cúbicos": lineal(1 / 28.3168),
    },
    "Monedas": {
        "Pesos a Dólares": lineal(1 / PESOS_POR_USD),
        "Pesos a Reales": lineal(1 / PESOS_POR_BRL),
        "Pesos a Euros": lineal(1 / PESOS_POR_EUR),
    },
    "Informática": {
        "B a KB": lineal(1 / 1024),
        "KB a MB": lineal(1 / 1024),
        "MB a GB": lineal(1 / 1024),
        "GB a TB": lineal(1 / 1024),
    },
}


def formato(n):
    """Número sin ceros de más (212.000000 -> 212)."""
    if n == 0:
        return "0"
    if abs(n) >= 0.0001:
        return f"{n:.6f}".rstrip("0").rstrip(".")
    return f"{n:.6g}"


# ---------------- Lógica ----------------
actualizando = False  # evita que al escribir un Entry se dispare el otro


def calcular(sentido):
    """sentido 'ida': origen -> destino. 'vuelta': destino -> origen."""
    global actualizando
    if actualizando or not combo.get():
        return

    ida, vuelta = CONVERSIONES[categoria.get()][combo.get()]
    if sentido == "ida":
        var_entrada, var_salida, funcion = v_origen, v_destino, ida
    else:
        var_entrada, var_salida, funcion = v_destino, v_origen, vuelta

    texto = var_entrada.get().strip().replace(",", ".")
    if texto in ("", "-", ".", "-."):
        error.config(text="")
        actualizando = True
        var_salida.set("")
        actualizando = False
        return

    try:
        numero = float(texto)
    except ValueError:
        error.config(text="Número no válido")
        return

    error.config(text="")
    actualizando = True
    var_salida.set(formato(funcion(numero)))
    actualizando = False


def cambiar_conversion(*args):
    origen, destino = combo.get().split(" a ")
    lbl_origen.config(text=origen)
    lbl_destino.config(text=destino)
    calcular("ida")


def cambiar_categoria(*args):
    combo["values"] = list(CONVERSIONES[categoria.get()])
    combo.current(0)
    cambiar_conversion()


# ---------------- Ventana ----------------
app = tk.Tk()
app.title("Unidades de Medida")
app.configure(bg=FONDO)
app.minsize(600, 560)

# Colores de la lista que se despliega en el Combobox
app.option_add("*TCombobox*Listbox.background", COLOR)
app.option_add("*TCombobox*Listbox.foreground", "white")
app.option_add("*TCombobox*Listbox.selectBackground", CLARO)
app.option_add("*TCombobox*Listbox.selectForeground", "white")
app.option_add("*TCombobox*Listbox.font", ("Winkle", 11))

# Estilo del Combobox
estilo = ttk.Style()
estilo.theme_use("clam")
estilo.configure("Verde.TCombobox", fieldbackground=COLOR, background=COLOR,
                 foreground="white", arrowcolor="white", bordercolor=COLOR,
                 lightcolor=COLOR, darkcolor=COLOR, padding=6)
estilo.map("Verde.TCombobox",
           fieldbackground=[("readonly", COLOR)],
           foreground=[("readonly", "white")],
           selectbackground=[("readonly", COLOR)],
           selectforeground=[("readonly", "white")])

fuente = ("Winkle", 11)

tk.Label(app, text="CALCULADORA", font=("Winkle", 40),
         fg=COLOR, bg=FONDO).pack(pady=(25, 15))

# Categoría (OptionMenu)
tk.Label(app, text="Categoría:", font=fuente, bg=FONDO, fg="white").pack()
categoria = tk.StringVar(value=list(CONVERSIONES)[0])
menu = tk.OptionMenu(app, categoria, *CONVERSIONES, command=cambiar_categoria)
menu.config(width=30, font=fuente, bg=COLOR, fg="white", activebackground=CLARO,
            activeforeground="white", relief="flat", highlightthickness=0)
menu["menu"].config(bg=COLOR, fg="white", activebackground=CLARO,
                    activeforeground="white", font=fuente)
menu.pack(pady=(0, 12))

# Conversión (Combobox)
tk.Label(app, text="Conversión:", font=fuente, bg=FONDO, fg="white").pack()
combo = ttk.Combobox(app, state="readonly", width=32, font=fuente,
                     style="Verde.TCombobox")
combo.pack(pady=(0, 18))
combo.bind("<<ComboboxSelected>>", cambiar_conversion)


# Dos Entry, uno por cada unidad (se escribe en cualquiera)
def fila(variable, sentido):
    marco = tk.Frame(app, bg=FONDO)
    marco.pack(pady=4)
    entrada = tk.Entry(marco, textvariable=variable, font=("Winkle", 14),
                       width=16, bg="white", fg="black", relief="flat",
                       highlightthickness=2, highlightbackground=COLOR,
                       highlightcolor=COLOR, insertbackground=COLOR)
    entrada.pack(side="left", ipady=6)
    unidad = tk.Label(marco, text="", font=("Winkle", 13, "bold"), width=12,
                      anchor="w", bg=FONDO, fg="white")
    unidad.pack(side="left", padx=(10, 0))
    variable.trace_add("write", lambda *args: calcular(sentido))
    return entrada, unidad


v_origen = tk.StringVar()
v_destino = tk.StringVar()

entrada_origen, lbl_origen = fila(v_origen, "ida")
tk.Label(app, text="=", font=("Winkle", 16, "bold"), bg=FONDO,
         fg=COLOR).pack()
entrada_destino, lbl_destino = fila(v_destino, "vuelta")

error = tk.Label(app, text="", font=fuente, bg=FONDO, fg="#FFB3B3")
error.pack(pady=10)

cambiar_categoria()
entrada_origen.focus_set()
app.mainloop()