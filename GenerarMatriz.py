import numpy as np

def GenerarMatriz(palabra):
    MatrizFinal =  ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","W ","X","Y","Z"]
    palabra_Clave = str(palabra).upper()
    Palabra = list(palabra_Clave)

    #Eliminar elementos repetidos de la palabra
    palabra_Procesada = []
    for element in Palabra:
        if element not in palabra_Procesada:
            palabra_Procesada.append(element)
    len_Palabra = len(palabra_Procesada)
    palabra_Procesada.reverse()

    #Eliminamos las letras de la palabra que esten en la matriz
    for i in range (len_Palabra):
        if palabra_Procesada[i] in MatrizFinal:
            MatrizFinal.remove(palabra_Procesada[i])
    
    #Agregar los elementos de la palabra al alfabeto
    for j in range (len_Palabra):
        MatrizFinal.insert(0,palabra_Procesada[j])
        j += 1

    #Convertimos la lista un array de numpy y le damos forma de matriz (5x5)
    MatrizFinal = np.array(MatrizFinal)
    MatrizFinal = MatrizFinal.reshape(5,5)

    return(MatrizFinal)

if __name__ == '__main__':
    Matriz = GenerarMatriz("SAluDOs")
    print(Matriz)