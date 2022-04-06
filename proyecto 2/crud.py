from tkinter import *
from tkinter import messagebox
import pymysql
####################Conexion  a la base de datos###################
conexion = pymysql.connect(
    host="localhost",
    user="root",
    passwd="edison",
    db="CRUD1",
    port=3334
)

root = Tk()
root.title("CRUD ")
#VARIABLES
id=StringVar()
nombre=StringVar()
edad=StringVar()
usuario=StringVar()
contraseña=StringVar()
#Frame1
miFrame1=Frame(root)
miFrame1.pack()
#labels
labelId=Label(miFrame1, text="ID ")
labelId.grid(row=1, column=1, padx=10, pady=10, sticky="e")
labelNombre=Label(miFrame1, text="Nombre ")
labelNombre.grid(row=2, column=1, padx=10, pady=10, sticky="e")
labelEdad=Label(miFrame1, text="Edad ")
labelEdad.grid(row=3, column=1, padx=10, pady=10, sticky="e")
labelUsuario=Label(miFrame1, text="Usuario ")
labelUsuario.grid(row=4, column=1, padx=10, pady=10, sticky="e")
labelContraseña=Label(miFrame1, text="Contraseña ")
labelContraseña.grid(row=5, column=1, padx=10, pady=10, sticky="e")
#cuadros
entryId=Entry(miFrame1, textvariable=id)
entryId.grid(row=1, column=2, padx=10, pady=10)
entryNombre=Entry(miFrame1, textvariable=nombre)
entryNombre.grid(row=2, column=2, padx=10, pady=10)
entryEdad=Entry(miFrame1, textvariable=edad)
entryEdad.grid(row=3, column=2, padx=10, pady=10)
entryUsuario=Entry(miFrame1, textvariable=usuario)
entryUsuario.grid(row=4, column=2, padx=10, pady=10)
entryContraseña=Entry(miFrame1, textvariable=contraseña)
entryContraseña.grid(row=5, column=2, padx=10, pady=10)

#dando definiciones a los botones
def codCrear():
    datosC = id.get(), nombre.get(), edad.get(), usuario.get(), contraseña.get()
    #idC=id.get()
    #nomC=nombre.get()
    #edC=edad.get()
    #usuC=usuario.get()
    #conC=contraseña.get()

    curCrear=conexion.cursor()
    curCrear.execute("INSERT INTO PERSONA VALUES {}".format(datosC))
    conexion.commit()
    #conexion.close()
    print("Creado exitosamente")
    limpiar()
    
    
def codLeer():
    id1=id.get()
    curLeer=conexion.cursor()
    curLeer.execute("SELECT IDPERSONA, NOMBRE, EDAD, USUARIO, CONTRASENA FROM PERSONA WHERE IDPERSONA = "+ id1)
    for IDPERSONA, NOMBRE, EDAD, USUARIO, CONTRASENA in curLeer.fetchall():
        print(IDPERSONA, NOMBRE, EDAD, USUARIO, CONTRASENA)

        nombre.set(NOMBRE)
        edad.set(EDAD)
        usuario.set(USUARIO)
        contraseña.set(CONTRASENA)
        #conexion.close()

def codActualizar():
    datosA = [nombre.get(), edad.get(), usuario.get(), contraseña.get(), id.get()]
    #idA=id.get()
    #nomA=nombre.get()
    #edA=edad.get()
    #usuA=usuario.get()
    #conA=contraseña.get()

    curActualizar=conexion.cursor()
    #curActualizar.execute("UPDATE PERSONA SET NOMBRE={}, EDAD={}, USUARIO={}, CONTRASENA={} WHERE IDPERSONA={}".format(nomA, edA, usuA, conA, idA))
    curActualizar.execute("UPDATE PERSONA SET NOMBRE=%s, EDAD=%s, USUARIO=%s, CONTRASENA=%s WHERE IDPERSONA=%s", datosA)
    conexion.commit()
    limpiar()
    #conexion.close()
    print("Actualizacion exitosa")

def codEliminar():
    curElim=conexion.cursor()
    curElim.execute("DELETE FROM PERSONA WHERE IDPERSONA=%s", id.get())
    conexion.commit()
    limpiar()
    print("Eliminado con exito")

#FRAME2
miFrame2=Frame(root)
miFrame2.pack()
#botones
btnCrear=Button(miFrame2, text="Crear", cursor="hand2", command=codCrear)
btnCrear.grid(row=1, column=1, padx=10, pady=10)
btnLeer=Button(miFrame2, text="Leer", cursor="hand2", command=codLeer)
btnLeer.grid(row=1, column=2, padx=10, pady=10)
btnActualizar=Button(miFrame2, text="Actualizar", cursor="hand2", command=codActualizar)
btnActualizar.grid(row=1, column=3, padx=10, pady=10)
btnEliminar=Button(miFrame2, text="Eliminar", cursor="hand2", command=codEliminar)
btnEliminar.grid(row=1, column=4, padx=10, pady=10)

############33FUNCIONES PARA MENU VAR##################
#limbiar
def limpiar():
    id.set("")
    nombre.set("")
    edad.set("")
    usuario.set("")
    contraseña.set("")
#mensaje
def mensaje():
    messagebox.showinfo("Acerca", """ 
    CRUD
    Version 1
    Unsando Tkinter y mysql
    Hecho por Edison Velasco Huaman
    """)
#Salir
def salir():
    root.destroy()
#############MENU BAR#################################
menuBar=Menu(root)
menu1=Menu(menuBar, tearoff=0)
menu1.add_command(label="Limpiar", command=limpiar)
menu1.add_command(label="Acerca", command=mensaje)
menuBar.add_cascade(label="Inicio", menu=menu1)

#menu2=Menu(menuBar, tearoff=0)
#menu2.add_command(label="Salir", command=salir)
menuBar.add_command(label="Salir",command=salir)

root.config(menu=menuBar)

root.mainloop()