import tkinter as tk

ventana = tk.Tk() #Creo la ventana por TK

ventana.title("Mi Primera Ventana en TK") #Le pongo nombre a la ventana

ventana.geometry("720x480") #Indico el tamano de la ventana al a parecer

ventana.minsize(300, 300) #Minimo de la ventana
ventana.maxsize(970, 560) #Maximo de la ventana


ventana.configure(background="lightblue") #Color de fondo de la ventana


#A partado de frame

#Un frama es un espacio que se le asigna dentro de la ventana

frame1 = tk.Frame(ventana) #Declaro que voy a crear el freme (espacio) dentro de la ventana

frame1.pack() #El pack lo que hace es insertarlo en la ventana (es como guardar los cambios)

frame1.configure(background="yellow", width=400, height=200, bd=10)
#Le asigno color, alto, ancho y un borde

frame2 = tk.Frame(frame1) #Acá creamos un frame dentro de otro frame
frame2.configure(background="lightblue", width=100, height=100, bd=5)
frame2.pack()




ventana.mainloop()
