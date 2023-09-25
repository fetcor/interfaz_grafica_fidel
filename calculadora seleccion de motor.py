import tkinter as tk

ventana = tk.Tk()
ventana.title("calculadora")
ventana.geometry("800x800+700+100")
ventana.minsize(width=400, height=500)
ventana.configure(bg="lightblue")


### FUNCIONES ####

def calcular():
    try:
        tension1 = entrada_tension1.get()
        tension2 = entrada_tension2.get()
        velocidad = entrada_velocidad.get()
        eficiencia = entrada_eficiencia.get()

        resultado = ((float(tension1)-float(tension2))*float(velocidad))/(102*float(eficiencia))
        rotulo_resultado.config(text=resultado)
        
    except ValueError:
        if tension1== "":
            rotulo_resultado.config(text="¿dato?")

        
        elif tension2== "":
            rotulo_resultado.config(text="¿dato?")
        
        elif velocidad== "":
            rotulo_resultado.config(text="¿dato?")
        
        elif eficiencia== "":
            rotulo_resultado.config(text="¿dato?")
        else:
            rotulo_resultado.config(text="Error")

    finally:
        entrada_tension1.config(state = "disabled")
        entrada_tension2.config(state = "disabled")
        entrada_velocidad.config(state = "disabled")
        entrada_eficiencia.config(state = "disabled")
        boton_calcular.config(state= "disabled")

def borrar():
    entrada_tension1.config(state="normal")
    entrada_tension2.config(state="normal")
    entrada_velocidad.config(state="normal")
    entrada_eficiencia.config(state="normal")
    boton_calcular.config(state="normal")
    entrada_tension1.delete(0, tk.END)
    entrada_tension2.delete(0, tk.END)
    entrada_velocidad.delete(0, tk.END)
    entrada_eficiencia.delete(0, tk.END),
    rotulo_resultado.config(text="")
# entradas       

rotulo_titulo = tk.Label(ventana,
                         text="Seleccion de motor electrico",
                         bg="lightblue", fg="black",
                         font=("consolas",20, "bold"),
                         relief=tk.GROOVE, bd=2,
                         padx=20, pady=20)
rotulo_titulo.pack(padx=20, pady=20)

#frame primero
cuadro1 = tk.Frame(ventana,
                   bg="lightblue")

rotulo_sb1 = tk.Label(cuadro1,
                          text="Tension de vehiculo que asciende(kgf):",
                          bg="lightblue",
                          font=("consolas",10,"bold"),
                          width=40,
                          anchor=tk.W)
rotulo_sb1.pack(side=tk.LEFT, padx=20, pady=20)

entrada_tension1 = tk.Entry(cuadro1,
                           
                           bg="white", fg="black",
                           font=("consolas",18, "bold"),
                           relief=tk.SUNKEN, bd=3,
                           width=10,
                           justify=tk.RIGHT,
                           state="normal")
entrada_tension1.pack(side=tk.LEFT,padx=20, pady=20)

cuadro1.pack()

# frame segundo

cuadro2 = tk.Frame(ventana,
                   bg="lightblue")

rotulo_sb2 = tk.Label(cuadro2,
                          text="Tension de vehiculo que desciende(kgf):",
                          bg="lightblue",
                          font=("consolas",10,"bold"),
                          width=40,
                          anchor=tk.W)
                          
rotulo_sb2.pack(side=tk.LEFT, padx=20, pady=20)

entrada_tension2 = tk.Entry(cuadro2,
                           
                           bg="white", fg="black",
                           font=("consolas",18, "bold"),
                           relief=tk.SUNKEN, bd=3,
                           width=10,
                           justify=tk.RIGHT,
                           state="normal")
entrada_tension2.pack(side=tk.LEFT,padx=20, pady=20)

cuadro2.pack()

#frame tercero
cuadro3 = tk.Frame(ventana,
                   bg="lightblue")



rotulo_v3 = tk.Label(cuadro3,
                          text="Velocidad del vehiculo(m/s):",
                          bg="lightblue",
                          font=("consolas",10,"bold"),
                          width=40,
                          anchor=tk.W)
                          
rotulo_v3.pack(side=tk.LEFT, padx=20, pady=20)

entrada_velocidad = tk.Entry(cuadro3,
                           
                           bg="white", fg="black",
                           font=("consolas",18, "bold"),
                           relief=tk.SUNKEN, bd=3,
                           width=10,
                           justify=tk.RIGHT,
                           state="normal")
entrada_velocidad.pack(side=tk.LEFT,padx=20, pady=20)

cuadro3.pack()

#frame cuarto

cuadro4 = tk.Frame(ventana,
                   bg="lightblue")



rotulo_n4 = tk.Label(cuadro4,
                          text="Eficiencia:",
                          bg="lightblue",
                          font=("consolas",10,"bold"),
                          width=40,
                          anchor=tk.W)
                          
rotulo_n4.pack(side=tk.LEFT, padx=20, pady=20)

entrada_eficiencia = tk.Entry(cuadro4,
                           
                           bg="white", fg="black",
                           font=("consolas",18, "bold"),
                           relief=tk.SUNKEN, bd=3,
                           width=10,
                           justify=tk.RIGHT,
                           state="normal")
entrada_eficiencia.pack(side=tk.LEFT,padx=20, pady=20)

cuadro4.pack()

# FRAME QUINTO

cuadro5 = tk.Frame(ventana,
                   bg="lightblue")



rotulo_potencia = tk.Label(cuadro5,
                          text="potencia(kW):",
                          bg="lightblue",
                          font=("consolas",10,"bold"),
                          width=22,
                          anchor=tk.W)
                          
rotulo_potencia.pack(side=tk.LEFT, padx=20, pady=20)

rotulo_resultado = tk.Label(cuadro5,
                           text=" ",
                           bg="lightgreen", 
                           font=("consolas",18, "bold"),
                           relief=tk.GROOVE, 
                           width=20,
                           anchor=tk.E)
rotulo_resultado.pack(side=tk.LEFT,padx=20, pady=20)

cuadro5.pack()

cuadro6 = tk.Frame(ventana,
                   bg="lightblue")
boton_borrar = tk.Button(cuadro6,
                         text="Borrar",
                         bg="grey",
                         font=("consola", 18, "bold"),
                         width=10,
                         command=borrar)
boton_borrar.pack(side=tk.LEFT,padx=20,pady=20)

boton_calcular = tk.Button(cuadro6,
                         text="Calcular",
                         bg="orange",
                         font=("consola", 18, "bold"),
                         width=10,
                         state="normal",
                         command=calcular)
boton_calcular.pack(side=tk.LEFT,padx=20,pady=20)

cuadro6.pack()


ventana.mainloop()
