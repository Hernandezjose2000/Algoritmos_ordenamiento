def busqueda_binaria(lista:list) ->None:

    
    elemento_a_buscar = int(input("Por favor ingresa el numero que deseas ubicar "))
    intermedio = int(len(lista) / 2)
    elemento_encontrado = False

    while not elemento_encontrado:

        if lista[intermedio] > elemento_a_buscar and len(lista) !=1:
            lista = lista[0:intermedio]
            intermedio = int(len(lista)/2)

        elif lista[intermedio] < elemento_a_buscar and len(lista) !=1:
            lista = lista[intermedio:]
            intermedio = int(len(lista)/ 2)
        
        elif lista[intermedio] != elemento_a_buscar and len(lista) ==1:
            print("No hemos encontrado el valor solicitado")
            elemento_encontrado = True

        else:
            print("encontrado!", lista[intermedio])
            elemento_encontrado = True


def insertion_sort(lista_numeros:list) ->None:

    
    for posicion in range(1,len(lista_numeros)):
        while posicion >0:

            if lista_numeros[posicion-1] > lista_numeros[posicion]:
                valor_auxiliar = lista_numeros[posicion-1]
                lista_numeros[posicion-1] = lista_numeros[posicion]
                lista_numeros[posicion] = valor_auxiliar
                posicion = posicion -1
            
            else:
                posicion = 0


def bubble_sort(lista_numeros:list)->None:

    
    for vuelta in range(len(lista_numeros)):

        for elemento_actual in range(len(lista_numeros)-1):
            if lista_numeros[elemento_actual]>lista_numeros[elemento_actual+1]:
                valor_auxiliar = lista_numeros[elemento_actual]
                lista_numeros[elemento_actual] = lista_numeros[elemento_actual+1]
                lista_numeros[elemento_actual+1] = valor_auxiliar


def selection_sort(lista_numeros:list) ->None:


    for posicion_valor_minimo in range(len(lista_numeros)):
        posicion = posicion_valor_minimo
        valor_minimo = lista_numeros[posicion_valor_minimo]

        for posicion_actual in range(posicion_valor_minimo+1,len(lista_numeros))
            if lista_numeros[posicion_actual] < valor_minimo:
                posicion = posicion_actual
                valor_minimo = lista_numeros[posicion_actual]

        auxiliar = lista_numeros[posicion_valor_minimo]
        lista_numeros[posicion_valor_minimo] = valor_minimo
        lista_numeros[posicion] = auxiliar 


def main() ->None:

    lista_numeros = [10,1,9,2,3,8,4,7,5,6]
    #insertion_sort(lista_numeros)
    #bubble_sort(lista_numeros)
    selection_sort(lista_numeros)
    print(lista_numeros)
    #busqueda_binaria(lista_numeros)


main()
