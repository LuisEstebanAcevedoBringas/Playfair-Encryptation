from ProcesarMensaje import ProcesamientoMensaje
from GenerarMatriz import GenerarMatriz
import numpy as np

def CifrarPlayfair(mensaje, palabra):
    Palabra = ProcesamientoMensaje(palabra) #Preprocess the keywork
    Matriz = GenerarMatriz(Palabra) #Generate the key matrix
    MensajeProcesado =  ProcesamientoMensaje(mensaje) #Preprocess the message
    MensajeCodificado = [] #Declare an empty list where the encrypted message will be stored.
    ContadorFIlas = 0
    ContadorColumnas = 0
    MismaFila = True
    MismaColumna = True
    L1 = 0
    L2 = 1

    longitud = len(MensajeProcesado) #Obtain the length of the message already processed.

    for k in MensajeProcesado: #Obtain the position of each letter of the message in the matrix.
        Posicion1 = np.where(Matriz == MensajeProcesado[ L1 ]) #Obtain the position of the letter 1 in the matrix
        Posicion2 = np.where(Matriz == MensajeProcesado[ L2 ]) #Obtain the position of the letter 2 in the matrix
        PosicionFila_Letra1 = int(Posicion1[0][0]) #Obtain the row where the letter 1 is in the matrix
        PosicionColumna_Letra1 = int(Posicion1[1][0]) #Obtain the column where the letter 1 is in the matrix
        PosicionFila_Letra2 = int(Posicion2[0][0]) #Obtain the row where the letter 2 is in the matrix
        PosicionColumna_Letra2 = int(Posicion2[1][0]) #Obtain the column where the letter 2 is in the matrix

        #Find if the pair of letters are in the same row
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
        ContadorFIlas = 0 #Reset the counter
        
        #Find if the pair of letters are in the same column
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
        ContadorColumnas = 0 #Reset the counter

        #Look for combinations of letters that are not in the same row or column.
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

    MensajeFinal = "".join(MensajeCodificado) #Pass the list to a string
    return(MensajeFinal)