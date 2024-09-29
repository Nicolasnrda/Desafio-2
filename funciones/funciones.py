#1)
from UTN_Heroes_Dataset.utn_matrices import matriz_data_heroes
from UTN_Heroes_Dataset.utn_funciones.auxiliares import color_text



def mostrar_heroe(matriz, sub_indice, indice) -> str:
    texto = ""
    texto_original = matriz[sub_indice][indice]

    match texto_original:
                case str():
                    if len(texto_original) >= 20:
                        texto_saneado = texto_original[0:20-1]
                        texto += f"{texto_saneado:{20}} | "
                    else: 
                        texto += f"{texto_original:{20}} | "
                case int():
                    texto += f"{matriz[sub_indice][indice]:03} | "
                case float():
                    texto += f"{matriz[sub_indice][indice]:05.2f} | "
                case _:
                    texto += f"{matriz[sub_indice][indice]} | "
    return texto
    

def matriz_con_todos_los_heroes(matriz):

    cantidad_columnas = len(matriz[0])
    cantidad_filas = len(matriz)

    for indice in range(cantidad_columnas):
        texto = ""
        for sub_indice in range(cantidad_filas):

            texto += f"{mostrar_heroe(matriz, sub_indice, indice)}"

        texto = texto[0:-3]
        print(texto) 

#Ejercicio 1 y 2
def mostrar_por_genero(matriz:list[list], genero: str) -> list:
    """Esta funcion lo que hace es filtrar a los heroes segun su genero

    Args:
        matriz (list[list]): Recibe la matriz con todos sus datos
        genero (str): Recibe el genero a filtrar

    Returns:
        list: Devuelve la lista de heroes con ese genero
    """
    cantidad_columnas = len(matriz[0])
    cantidad_filas = len(matriz)
    for indice in range(cantidad_columnas):
        texto = ""
        if(matriz[3][indice] == genero):
            for sub_indice in range(cantidad_filas):
                texto += f"{mostrar_heroe(matriz, sub_indice, indice)}"
            texto = texto[0:-3]
            print(texto)       

#Ejercicio 3)
def mas_de_setentaycinco_en_poder(matriz:list[list]) -> list:
    """
    Lo que hace esta funcion es mostrar los heroes con poder mayor a 75
    Args:
        matriz (list[list]): Recibe la matriz con los heroes

    Returns:
        list: Devuelve la lista de heroes con mas de ese poder
    """
    cantidad_columnas = len(matriz[0])
    cantidad_filas = len(matriz)
    for indice in range(cantidad_columnas):
        texto = ""
        if(matriz[4][indice] >= 75):
            for sub_indice in range(cantidad_filas):
                texto += f"{mostrar_heroe(matriz, sub_indice, indice)}"
            texto = texto[0:-3]
            print(texto)

#Ejercicio 4) 

def mas_de_cientosesenta_de_altura(matriz:list[list]) -> list:
    """Esta funcion muestra a los heroes con altura mayor a 160

    Args:
        matriz (list[list]): Recibe la matriz con los heroes

    Returns:
        list: Devuelve la lista de heroes con mas de esa altura
    """
    cantidad_columnas = len(matriz[0])
    cantidad_filas = len(matriz)
    for indice in range(cantidad_columnas):
        texto = ""
        if(matriz[5][indice] >= 160):
            for sub_indice in range(cantidad_filas):
                texto += f"{mostrar_heroe(matriz, sub_indice, indice)}"
            texto = texto[0:-3]
            print(texto)

#Ejercicio 5)
def femenino_mas_60(matriz:list[list], genero: str) -> list:
    """Esta funcion lo que hace es filtrar a los heroes femeninos mayores a 60 de poder

    Args:
        matriz (list[list]): Recibe la matriz con todos sus datos
        genero (str): Recibe el genero a filtrar
        poder(int): Recibe valor de poder a filtrar
    Returns:
        list: Devuelve la lista de heroes femeninos con mas de 60 de poder
    """
    cantidad_columnas = len(matriz[0])
    cantidad_filas = len(matriz)
    for indice in range(cantidad_columnas):
        texto = ""
        if(matriz[3][indice] == genero and matriz[4][indice] <= 60 ):
            for sub_indice in range(cantidad_filas):
                texto += f"{mostrar_heroe(matriz, sub_indice, indice)}"
            texto = texto[0:-3]
            print(texto)                

#Ejercicio 6) 

def masculino_menos_60(matriz:list[list], genero: str) -> list:
    """Esta funcion lo que hace es filtrar a los heroes masculino menores a 60 de poder

    Args:
        matriz (list[list]): Recibe la matriz con todos sus datos
        genero (str): Recibe el genero a filtrar
        poder(int): Recibe valor de poder a filtrar
    Returns:
        list: Devuelve la lista de heroes masculinos con menos de 60 de poder
    """
    cantidad_columnas = len(matriz[0])
    cantidad_filas = len(matriz)
    for indice in range(cantidad_columnas):
        texto = ""
        if(matriz[3][indice] == genero and matriz[4][indice] >= 60 ):
            for sub_indice in range(cantidad_filas):
                texto += f"{mostrar_heroe(matriz, sub_indice, indice)}"
            texto = texto[0:-3]
            print(texto)       

#Ejercicio 7)

#def personajes_NoBinarios_10_y_50_inclusive( matriz:list[list],genero:str, poder:int) -> list:
#    """Esta funcion lo que hace es filtrar a los heroes No-Binarios con poder entre 10 y 50 inclusive.
#
#    Args:
#        matriz (list[list]):Recibr la matriz con todo sus datos 
#        genero (str):Recibe el genero a filtrar
#        poder_minimo(int): Recibe el valor de poder minimo a filtrar
#        poder_max(int): Recibe el valor de poder maximo a filtrar    
#    Returns:
#        list:Devuelve la lista de No-Binarios con poder entre 10 y 50 inclusive
#    """
#    cantidad_columnas = len(matriz[0])
#    cantidad_filas = len(matriz)
#    for indice in range (cantidad_columnas):
#        texto= ""
#        if (matriz[3][indice] == genero and poder[4][indice] and poder[4][indice] <=50 ):
#            for sub_indice in range(cantidad_filas):
#                texto += f"{mostrar_heroe(matriz, sub_indice, indice)}"
#            texto=texto[0:-3]
#            print(texto)


##Ejercicio 8)
#def minimo_poder(matriz:list[list]) -> list:
#    """ Esta funcion lo que hace es buscar el poder minimo de poder y mostrar cuantos heroes tienen un poder igual al minimo
#
#    Args:
#        matriz (list[list]):Recibe la matriz con todos sus datos 
#        poder_minimo (int):Recibe el valor de poder minimo y busca cuantos heroes tiene el mismo poder 
#
#    Returns:
#        list:Devuelve la lista con el poder minimo de poder y muestra cuantos heroes tienen un poder igual al minimo
#    """
#    cantidad_columnas = len(matriz[0])
#    cantidad_filas = len(matriz)
#    poder_minimo = min(min(fila) for fila in matriz)
#    lista_menor_poder = []
#    for indice in range (cantidad_columnas):
#        contador_poder_minimo = []
#        texto="" 
#        if(matriz[4][indice] == poder_minimo):
#            print(poder_minimo)
#            contador_poder_minimo += matriz
#            for sub_indice in range(cantidad_filas):
#                texto += f"{mostrar_heroe(matriz, sub_indice, indice)}"
#            texto=texto[0:-3]
#            print(texto)
#minimo_poder(matriz_data_heroes)
#


#Ejercicio 10)
#
#def orden_alfabetico_ascendente(matriz:list[list]) -> list:
#    """Esta funcion ordena alfabeticamente ascendete a los heroes segun su nombre
#
#    Args:
#        matriz (list[list]): Recibe la matriz con los heroes
#
#    Returns:
#        list: Devuelve la lista de heroes ordenda alfabeticamente ascendente
#    """
#    cantidad_columnas = len(matriz[0])
#    cantidad_filas = len(matriz)
#    for indice in range (cantidad_columnas):
#        texto= ""
#        if matriz.sort():
#            for sub_indice in range(cantidad_filas):
#                texto += f"{mostrar_heroe(matriz, sub_indice, indice)}"
#            texto=texto[0:-3]
#            print(texto)
#



#def obtener_poder_minimo(matriz:list[list]) -> float:
#    """
#
#    Args:
#        lista_numerica (list): _description_ Una lista numerica la cual
#        tiene que iterar para encontrar el numero mas grande
#
#    Returns:
#        float: _description_ El numero mas grande de la lista, parseado a 
#        flotante
#    """
#    minimo = None 
#    cantidad_columnas = len(matriz[0])
#    cantidad_filas = len(matriz)
#    for indice in range(cantidad_columnas):
#        texto= ""
#        if cantidad_columnas[4] not minimo or minimo > indice:
#            minimo = indice 
#            for sub_indice in range(cantidad_filas):
#                texto += f"{mostrar_heroe(matriz, sub_indice, indice)}"
#            texto=texto[0:-3]
#            print(texto)
#
#obtener_poder_minimo(matriz_data_heroes)
