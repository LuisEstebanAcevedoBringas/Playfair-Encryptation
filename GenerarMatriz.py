import numpy as np

def GenerarMatriz(palabra):
    MatrizFinal =  ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","W ","X","Y","Z"]
    palabra_Clave = str(palabra).upper()
    Palabra = list(palabra_Clave)

    #Remove repeated word elements
    palabra_Procesada = []
    for element in Palabra:
        if element not in palabra_Procesada:
            palabra_Procesada.append(element)
    len_Palabra = len(palabra_Procesada)
    palabra_Procesada.reverse()

    #Eliminate the letters of the word that are in the matrix.
    for i in range (len_Palabra):
        if palabra_Procesada[i] in MatrizFinal:
            MatrizFinal.remove(palabra_Procesada[i])
    
    #Adding word elements to the alphabet
    for j in range (len_Palabra):
        MatrizFinal.insert(0,palabra_Procesada[j])
        j += 1

    #Convert the list to a numpy array and give it the form of a matrix (5x5).
    MatrizFinal = np.array(MatrizFinal)
    MatrizFinal = MatrizFinal.reshape(5,5)

    return(MatrizFinal)

if __name__ == "__main__":
    x = GenerarMatriz("hola")
    print(x)