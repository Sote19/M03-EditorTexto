#Librerias
from tkinter import *
from tkinter import filedialog as fd#Tratar rutas de archivos
from tkinter import messagebox
import formatos
#Para guardar PDF
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
#Estructura basica para usar Tkinter
root=Tk()
root.title("Editor de texto ~ Soteras ~")

"""
FUNCIONES
"""
#Funcion para las rutas de los archivos 
ruta_archivo= ''
#Funcion para NUEVOS archivos
def nuevo():
    mensaje.set('Nuevo fichero')#Modificar el texto inferior, se aplicara en cada funcion
    texto.delete(1.0, END)#Para que borre desde el primer caracter hasta el ultimo
#Funcion para ABRIR archivos
def abrir():
    global ruta_archivo #Para que dentro de la funcion, se trate la variable de fuera de la funcion
    mensaje.set('Nuevo fichero')
    texto.delete(1.0,END)
    root.title("Editor de texto ~ Soteras ~")
    ruta_archivo=""
    
    ruta_archivo=fd.askopenfilename(
        initialdir='.',#Abre el directorio actual
        filetypes=(("Ficheros de texto", "*.txt"),),#Muestra solo, este tipo de archivos
        title="Elige el fichero que quieres abrir"#Texto que se muestra
    )
    
    if ruta_archivo != "":#Si la ruta no esta vacia...
        archivo=open(ruta_archivo,'r')#r para obligar a pulsar en la hoja, para realizar cambios
        contenido=archivo.read()
        texto.delete(1.0,'end')#Borre contenido actual, antes de abrir
        texto.insert('insert',contenido)
        archivo.close()
        root.title(ruta_archivo + " | Editor de texto ~ Soteras ~") #Para saber que ruta estamos modificando
        
#Funcion para GUARDAR archivos
def guardar():
    global ruta_archivo
    mensaje.set('Guardar fichero')
    if ruta_archivo != "":#Si la ruta del archivo es correcta
        contenido=texto.get(1.0, 'end-1c')
        archivo=open(ruta_archivo, 'w+')#Abrir el archivo en modo escritura
        archivo.write(contenido)
        archivo.close()
    else:
        guardar_como()

#Funcion para GUARDAR COMO
def guardar_como():
    global ruta_archivo
    archivo=fd.asksaveasfile(title="Guardar fichero como...", mode='w', defaultextension=".txt")#Ventana emergente
    ruta_archivo=archivo.name
    if archivo is not None:
        contenido=texto.get(1.0, 'end-1c')
        archivo=open(ruta_archivo, 'w+')
        archivo.write(contenido)
        archivo.close()
        mensaje.set('Fichero guardado correctamente')
    else:
        mensaje.set('Guardado no realizado')

#Funcion CONFIRMAR AL SALIR
def cerrar_aplicacion():
    respuesta=messagebox.askyesno("Salir de la aplicacion", "¿Desea guardar el documento antes de salir?")
    if respuesta is True:
        guardar_como()
        root.quit()
    elif respuesta is False:
        root.quit()
    else:
        pass
root.protocol("WM_DELETE_WINDOW", cerrar_aplicacion)
#Funcio GUARDAR PDF "Per afegir aquesta funcio, he necesitat que la corregis chatgpt, ja que hi habia un bug"
def PDF():
    global ruta_archivo
    ruta_pdf=fd.asksaveasfilename(
        title="Guardar PDF...",
        filetypes=(("PDF files", ".pdf"),("All files", "*.*")),
        defaultextension=".pdf"
        )
    if ruta_pdf:
        c=canvas.Canvas(ruta_pdf, pagesize=letter)
        contenido=texto.get(1.0, END)
        c.drawString(100, 700, contenido)
        c.showPage()
        c.save()
        mensaje.set('PDF Creado')
    else:
        mensaje.set('PDF No creado')
        
#----------FUNCIONES DE FORMATO ----------
def usar_negrita(event=None):#Para que no espere argumentos
    try:
        #Bucle para al aplicar negrita a texto negrita = volver al normal
        if "negrita" in texto.tag_names("sel.first"):
            texto.tag_remove("negrita", "sel.first", "sel.last")
        else:
            formatos.negrita(texto)
    except TclError:
        pass

def usar_kursiva(event=None):
        #Bucle para al aplicar kursiva a texto Kursiva = volver al normal
    if "cursiva" in texto.tag_names("sel.first"):
        texto.tag_remove("cursiva", "sel.first", "sel.last")
    else:
        formatos.kursiva(texto)
    
def usar_subrayado(event=None):
        #Bucle para al aplicar subray a texto subray = volver al normal
    if "subrayado" in texto.tag_names("sel.first"):
        texto.tag_remove("subrayado", "sel.first", "sel.last")
    else:
        formatos.subrayado(texto)

def usar_neku(event=None):
        #Bucle para aplicar negrita y cursiva juntas
    if "neku" in texto.tag_names("sel.first"):
        texto.tag_remove("neku", "sel.first", "sel.last")
    else:
        formatos.neku(texto)
                    
#Menu superior sencillo
princip_menu=Menu(root)
menuopcion=Menu(princip_menu, tearoff=1) #Permitimos poder desprender el menu, al usuario
#Menu Archivo
princip_menu.add_cascade(label="Opciones", menu=menuopcion)#Desplegar menu
menuopcion.add_command(label="Nuevo", command=nuevo)#Blanco doc
menuopcion.add_command(label="Abrir archivo", command=abrir)#Abrir doc
menuopcion.add_separator()
menuopcion.add_command(label="Guardar archivo", command=guardar)#Guardar doc
menuopcion.add_command(label="Guardar como...", command=guardar_como)#Crear doc
menuopcion.add_separator()
menuopcion.add_command(label="Eliminar archivo")#Eliminar doc
menuopcion.add_command(label="Salir", command=root.quit)#Cerrar app
#Menu formatos
menuformatos=Menu(princip_menu, tearoff=0)
princip_menu.add_cascade(label="Formatos", menu=menuformatos)
menuformatos.add_command(label="Negrita ----- Cntrl+B", command=usar_negrita)
menuformatos.add_command(label="Kursiva ----- Cntrl+L", command=usar_kursiva)#El kursiva con tecla rapida, daba un error que me fue imposible solucionar, asi que decidi eliminarlo
menuformatos.add_command(label="Subray  ----- Cntrl+U", command=usar_subrayado)
menuformatos.add_command(label="Negrita Kursiva -----Cntrl+P", command=usar_neku)
#PDF
formato_pdf=Menu(princip_menu, tearoff=0)
princip_menu.add_command(label="Guardar PDF", command=PDF)

#Bindeos de teclas
root.bind("<Control-b>", usar_negrita)
root.bind("<Control-l>", usar_kursiva)
root.bind("<Control-u>", usar_subrayado)

#Hoja en la que escribiremos
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(padx=6, pady=4, font=('Arial',12))

#Textos de ayuda, en la parte inferior de la hoja
mensaje = StringVar()
mensaje.set("Empieza a editar tu texto ;)")
monitor = Label(root, textvar=mensaje, justify='left')
monitor.pack(side="left")
        
#Bucle del menu
root.config(menu=princip_menu)
root.mainloop()