def ProcesamientoMensaje (mensaje):
    p = 0
    q = 1
    Mensaje = mensaje.replace(" ","").upper()
    print(Mensaje)

    #Eliminamos las letras con acentos, cambiamos a "v" por "u" y pasamos todo a mayusculas
    Acentos = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("v","u"),
        ("Á","A"),
        ("É","E"),
        ("Í","I"),
        ("Ó","O"),
        ("Ú","U"),
        ("V","U"))
    for a,b in Acentos:
        Mensaje = Mensaje.replace(a,b)
    ListaMensaje = list(Mensaje)
    longitud = len(ListaMensaje)

    #Si el mensaje solo es 1 letra se le agrega una "x" al final
    if longitud == 1:
        ListaMensaje.append("X")

    #Comprobamos si hay letras repetidas, si las hay se inserta una X entre las letras repetidas
    for k in ListaMensaje: 
        if ListaMensaje[p] == ListaMensaje [q]:
            ListaMensaje.insert(q,"X")
        p += 1
        q += 1
        if   q >= longitud: 
            break
    
    longitud = len(ListaMensaje) #Actualizamos la longitud de la lista

    if longitud % 2 != 0: #Comprobamos si el numero de letras en le mensaje es par, si no lo es se agrega una x al final
        ListaMensaje.append("X")

    return ListaMensaje

if __name__ == '__main__':
    
    Mensaje = input("Ingrese el mensaje: ")
    M = ProcesamientoMensaje(Mensaje)
    print(M)