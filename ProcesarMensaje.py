import string
import re

def ProcesamientoMensaje(mensaje):
    p = 0
    q = 1
    Mensaje = mensaje.replace(" ","").upper() #Remove the spaces and convert the string to uppercase.
    Mensaje = ''.join([i for i in Mensaje if not i.isdigit()]) #Remove digits from the message
    pattern = r'[' + string.punctuation + ']'
    Mensaje = re.sub(pattern, '', Mensaje) #Remove special characters from the message

    #Remove the letters with accents, change "v" to "u" and "ñ" to "n". 
    Acentos = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("v","u"),
        ("ñ","n"),
        ("Á","A"),
        ("É","E"),
        ("Í","I"),
        ("Ó","O"),
        ("Ú","U"),
        ("V","U"),
        ("Ñ","N"))
    for a,b in Acentos:
        Mensaje = Mensaje.replace(a,b)
    ListaMensaje = list(Mensaje)
    longitud = len(ListaMensaje)

    #If the message is only 1 letter, an "x" is added at the end.
    if longitud == 1:
        ListaMensaje.append("X")

    #We check if there are repeated letters, if there are, we insert an X between the repeated letters.
    for k in ListaMensaje: 
        if ListaMensaje[p] == ListaMensaje [q]:
            ListaMensaje.insert(q,"X")
        p += 1
        q += 1
        if   q >= longitud: 
            break
    
    longitud = len(ListaMensaje) #Ppdate the length of the list.

    if longitud % 2 != 0: #We check if the number of letters in the message is even, if it is not, we add an x at the end.
        ListaMensaje.append("X")

    return ListaMensaje

if __name__ == "__main__":
    x = ProcesamientoMensaje("!!<31SalUDOS2 3al44 55MURNEy666<3132!&/(%$#(=????)(/&%$")
    print(x)