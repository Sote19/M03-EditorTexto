import tkinter.font as tkf

# Inicializamos la variable que almacenará todas las líneas
lista = []

# Empezamos el bucle principal
while True:
    #Hacemos que cada linea que añadimos, se vaya acumulandoappend
    definitiu = "\n".join(lista) 
    #Que todas las lineas acumuladas, las printee
    print('TEXTO ACTUAL >>>\n' + definitiu+ '\n')
    # Creamos el menu con las opciones
    print("""
        ¿QUE QUIERES HACER?
        a) Crear archivo
        b) Abrir archivo
        c) Eliminar archivo
    """)
    #Guardamos la opcion en la variable "respuesta"
    respuesta = str(input('Introduzca su opción: '))
    
    #Si la respuesta es "a"
    if respuesta == "a":
        #Guardamos el escrito en "linea" y la añadimos en la lista con .append
        linea = input('Escribe lo que deseas guardar: ')
        lista.append(linea)

    #Si respuesta es "b"
    elif respuesta == "b":
        #Si hay lineas que borrar...
        if lista:
            #Borramos la ultima linea de la lista, con .pop
            ultima_linea = lista.pop()
            #printeamos la ultima linea introducida, para saber que borramos
            print(f'La última línea "{ultima_linea}" ha sido borrada con éxito.')
        #Si no hay lineas para borrar, le decimos que no se puede borrar nada
        else:
            print('No hay líneas para borrar.')

    # Si respuesta es "c"
    elif respuesta == "c":
        #Si hay lineas, las mostramos todas
        if lista:
            print('Las líneas que escribió fueron:')
            for linea in lista:
                print(linea)
            #Salimos del bucle
            break
                
    # Si respuesta es "d"
    #No hemos conseguido que la funcion "d" funcionara, dejamos esto, pero nose que falla.
    elif respuesta == 'd':
        texto_fin = definitiu + ultima_linea
        for char in texto_fin:
            if char != "\n": 
                unicode = ord(char)
                hexadecimal = hex(unicode)
                print(f'Caracter{char}, Unicode{unicode}, Hexdecimal{hexadecimal}')     
    #Si la opcion introducida no es a,b o c. Imrpimimos lo siguiente
    else:
        print('Por favor, introduzca una opción válida.')

