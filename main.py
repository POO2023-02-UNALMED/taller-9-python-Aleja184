from tkinter import Tk, Button, Entry
import re
import tkinter

# Configuración ventana principal
root = Tk()
root.title("CalculadoraPOO")
root.resizable(0,0)
root.geometry("300x300")

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=0, pady=5)

for i in range(4):
    root.columnconfigure(i, weight=1)


def contiene_numeros(value):
    patron = r'[0-9]'
    return bool(re.search(patron,value))
numero1 = ""
numero2 = ""
operator = ""
resultado = 0.0
def operacion(value):
    global operator
    global numero1
    global numero2
    global resultado
    if((contiene_numeros(value)or value==".")and operator==""):
        numero1+=value
    elif(value!="=" and (not contiene_numeros(value)) and value!="."):
        operator = value
    if(operator!=""):
        if(contiene_numeros(value) or value=="."):
            numero2+=value
    pantalla.delete(0,tkinter.END)
    pantalla.insert(0,numero1+operator+numero2)
    if(value=="="):
        pantalla.delete(0,tkinter.END)
        if(operator=="+"):
            resultado = float(numero1)+float(numero2)
            pantalla.insert(0,str(resultado))
        elif(operator=="-"):
            resultado = float(numero1)-float(numero2)
            pantalla.insert(0,str(resultado))
        elif(operator=="/"):
            resultado = float(numero1)/float(numero2)
            pantalla.insert(0,str(resultado))
        elif(operator=="*"):
            resultado = float(numero1)*float(numero2)
            pantalla.insert(0,str(resultado))
    if(resultado !=0.0):
        numero1 = ""
        numero2 = ""
        operator = ""
        resultado = 0.0


# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2" ,command=lambda:operacion("1")).grid(row=1, column=0, padx=0, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2" ,command=lambda:operacion("2")).grid(row=1, column=1, padx=0, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2" ,command=lambda:operacion("3")).grid(row=1, column=2, padx=0, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2" ,command=lambda:operacion("4")).grid(row=2, column=0, padx=0, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2" ,command=lambda:operacion("5")).grid(row=2, column=1, padx=0, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2" ,command=lambda:operacion("6")).grid(row=2, column=2, padx=0, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2" ,command=lambda:operacion("7")).grid(row=3, column=0, padx=0, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2" ,command=lambda:operacion("8")).grid(row=3, column=1, padx=0, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2" ,command=lambda:operacion("9")).grid(row=3, column=2, padx=0, pady=1)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2" ,command=lambda:operacion("=")).grid(row=4, column=0, columnspan=2, padx=0, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2" ,command=lambda:operacion("."), borderwidth=0).grid(row=4, column=2, padx=0, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2" ,command=lambda:operacion("+")).grid(row=1, column=3, padx=0, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2" ,command=lambda:operacion("-")).grid(row=2, column=3, padx=0, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2" ,command=lambda:operacion("*")).grid(row=3, column=3, padx=0, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2" ,command=lambda:operacion("/")).grid(row=4, column=3, padx=0, pady=1)

root.mainloop()