import numpy as np

def CifrarPlayfair(mensaje, Matriz):
    MensajeProcesado = mensaje
    MensajeCodificado = [] #Declaramos una lista vacia donde se almacenera el mensaje cifrado
    ContadorFIlas = 0
    ContadorColumnas = 0
    MismaFila = True
    MismaColumna = True
    L1 = 0
    L2 = 1

    longitud = len(MensajeProcesado) #Obtenemos la longitud del mensaje ya procesado

    for k in MensajeProcesado: #Obtenemos la posicion de cada letra del mensaje en la matriz
        Posicion1 = np.where(Matriz == MensajeProcesado[ L1 ]) #Obtenemos la posicion de la letra 1 en la matriz
        Posicion2 = np.where(Matriz == MensajeProcesado[ L2 ]) #Obtenemos la posicion de la letra 2 en la matriz
        PosicionFila_Letra1 = int(Posicion1[0][0]) #Obtenemos la fila en donde esta la letra 1 en la matriz
        PosicionColumna_Letra1 = int(Posicion1[1][0]) #Obtenemos la columna en donde esta la letra 1 en la matriz
        PosicionFila_Letra2 = int(Posicion2[0][0]) #Obtenemos la fila en donde esta la letra 2 en la matriz
        PosicionColumna_Letra2 = int(Posicion2[1][0]) #Obtenemos la columna en donde esta la letra 2 en la matriz

        #Busca si el par de letras estan en la misma fila
        while ContadorFIlas <= 4: 
            if MensajeProcesado[ L1 ] in Matriz[ ContadorFIlas, ] and MensajeProcesado[ L2 ] in Matriz[ ContadorFIlas, ]:
                PosicionColumna_Letra1 += 1
                PosicionColumna_Letra2 += 1
                if PosicionColumna_Letra1 == 5:
                    Letra1 = Matriz [ ContadorFIlas, 0 ]
                    Letra2 = Matriz [ ContadorFIlas, PosicionColumna_Letra2 ]
                    MensajeCodificado.append(Letra1)
                    MensajeCodificado.append(Letra2)
                elif PosicionColumna_Letra2 == 5:
                    Letra1 = Matriz [ ContadorFIlas, PosicionColumna_Letra1 ]
                    Letra2 = Matriz [ ContadorFIlas, 0 ]
                    MensajeCodificado.append(Letra1)
                    MensajeCodificado.append(Letra2)
                else:
                    Letra1 = Matriz [ ContadorFIlas, PosicionColumna_Letra1 ]
                    Letra2 = Matriz [ ContadorFIlas, PosicionColumna_Letra2 ]
                    MensajeCodificado.append(Letra1)
                    MensajeCodificado.append(Letra2)
                MismaFila = True
                break
            else:
                MismaFila = False
            ContadorFIlas += 1
        ContadorFIlas = 0 #Reiniciamos el contador
        
        #Buscamos si el par de letras estan en la misma columna
        while ContadorColumnas <= 4:
            if MensajeProcesado[ L1 ] in Matriz[ :, ContadorColumnas ] and MensajeProcesado[ L2 ] in Matriz[ :, ContadorColumnas ]:
                PosicionFila_Letra1 += 1
                PosicionFila_Letra2 += 1
                if PosicionFila_Letra1 == 5:
                    Letra1 = Matriz [ 0 , ContadorColumnas ]
                    Letra2 = Matriz [ PosicionFila_Letra2 , ContadorColumnas ]
                    MensajeCodificado.append(Letra1)
                    MensajeCodificado.append(Letra2)
                elif PosicionFila_Letra2 == 5:
                    Letra1 = Matriz [ PosicionFila_Letra1 , ContadorColumnas ]
                    Letra2 = Matriz [ 0 , ContadorColumnas ]
                    MensajeCodificado.append(Letra1)
                    MensajeCodificado.append(Letra2)
                else:
                    Letra1 = Matriz [ PosicionFila_Letra1, ContadorColumnas ]
                    Letra2 = Matriz [ PosicionFila_Letra2 , ContadorColumnas ]
                    MensajeCodificado.append(Letra1)
                    MensajeCodificado.append(Letra2)
                MismaColumna = True
                break
            else:
                MismaColumna = False
            ContadorColumnas += 1
        ContadorColumnas = 0

        #Buscamos las combinaciones de las letras que no estan en la misma fila o columna
        if MismaFila == False and MismaColumna == False:
            NuevaColumna_Letra1 = PosicionColumna_Letra2
            NuevaColumna_Letra2 = PosicionColumna_Letra1
            Letra1 = Matriz [ PosicionFila_Letra1,NuevaColumna_Letra1 ]
            Letra2 = Matriz [ PosicionFila_Letra2, NuevaColumna_Letra2 ]
            MensajeCodificado.append(Letra1)
            MensajeCodificado.append(Letra2)

        L1 += 2 
        L2 += 2
        if   L2 > longitud: 
            break

    MensajeFinal = "".join(MensajeCodificado) #Pasamos la lista a un string
    return(MensajeFinal)