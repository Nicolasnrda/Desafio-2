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
        print(color_text(texto,"Success")) 

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
            print(color_text(texto,"Success"))
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
            print(color_text(texto,"Success"))

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
            print(color_text(texto,"Success"))

#Ejercicio 5)
def femenino_mas_60(matriz:list[list], genero:str ,poder:int) -> list:
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
        if(matriz[3][indice] == genero and matriz[4][indice] >= poder ):
            for sub_indice in range(cantidad_filas):
                texto += f"{mostrar_heroe(matriz, sub_indice, indice)}"
            texto = texto[0:-3]
            print(color_text(texto,"Success"))          


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
        if(matriz[3][indice] == genero and matriz[4][indice] <= 60 ):
            for sub_indice in range(cantidad_filas):
                texto += f"{mostrar_heroe(matriz, sub_indice, indice)}"
            texto = texto[0:-3]
            print(color_text(texto,"Success"))   

#Ejercicio 7)

def personajes_NoBinarios_10_y_50_inclusive( matriz:list[list],genero:str, poderMin:int, poderMax: int) -> list:
    """Esta funcion lo que hace es filtrar a los heroes No-Binarios con poder entre 10 y 50 inclusive.

    Args:
        matriz (list[list]):Recibr la matriz con todo sus datos 
        genero (str):Recibe el genero a filtrar
        poder_minimo(int): Recibe el valor de poder minimo a filtrar
        poder_max(int): Recibe el valor de poder maximo a filtrar    
    Returns:
        list:Devuelve la lista de No-Binarios con poder entre 10 y 50 inclusive
    """
    
    cantidad_columnas = len(matriz[0])
    cantidad_filas = len(matriz)
    for indice in range (cantidad_columnas):
        texto= ""
        if (matriz[3][indice] == genero and ( matriz[4][indice] >= poderMin and matriz[4][indice] <= poderMax ) ):
            for sub_indice in range(cantidad_filas):
                texto += f"{mostrar_heroe(matriz, sub_indice, indice)}"
            texto=texto[0:-3]
            print(color_text(texto,"Success"))


#ejercicio 8)
def heroes_con_poder_menor(matriz: list[list]) -> list:
    """Esta funcion lo que hace es buscar en la matriz cuales son los heroes con menor poder 

    Args:
        matriz (list[list]): Recibe la matriz con los datos de los heroes

    Returns:
        list: Retorna la lista de los heroes con ese poder
    """
    cantidad_columnas = len(matriz[0])
    cantidad_filas = len(matriz)
    minimo_poder = None

    for indice in range(cantidad_columnas):
        if not minimo_poder or minimo_poder > matriz[4][indice]:
            minimo_poder = matriz[4][indice]
    for indice in range(cantidad_columnas):
        texto = ""
        if matriz[4][indice] == minimo_poder:
            for sub_indice in range(cantidad_filas):
                texto += f"{mostrar_heroe(matriz, sub_indice, indice)}"
            texto = texto[0:-3]
            print(color_text(texto,"Success"))

#ejercicio 9)
def heroes_con_maximo_altura(matriz: list[list]) -> list:
    """Esta funcion lo que hace es buscar en la matriz cuales son los heroes con mayor altura

    Args:
        matriz (list[list]): Recibe la matriz con los datos de los heroes

    Returns:
        list: Retorna la lista de los heroes con esa altura
    """
    cantidad_columnas = len(matriz[0])
    cantidad_filas = len(matriz)
    maxima_altura = None
    for indice in range(cantidad_columnas):
        if not maxima_altura or maxima_altura < matriz[5][indice]:
            maxima_altura = matriz[5][indice]
    for indice in range(cantidad_columnas):
        texto = ""
        if matriz[5][indice] == maxima_altura:
            for sub_indice in range(cantidad_filas):
                texto += f"{mostrar_heroe(matriz, sub_indice, indice)}"
            texto = texto[0:-3]
            print(color_text(texto,"Success")) 
    
#Ejercicio 10)

def orden_alfabetico_ascendente(matriz:list[list]):
    """Esta funcion ordena alfabeticamente ascendete a los heroes segun su nombre

    Args:
    matriz (list[list]): Recibe la matriz con los heroes

    Returns:
    list: Devuelve la lista de heroes ordena alfabeticamente ascendente
    """
    cantidad_columnas = len(matriz[0])
    cantidad_filas = len(matriz)
    auxiliar = ""
    for indice in range (cantidad_columnas-1):
        for sub_indice in range(indice + 1,cantidad_columnas):
            if(matriz[0][indice] > matriz[0][sub_indice]):
                for filas in range(cantidad_filas):
                    auxiliar = matriz[filas][sub_indice]
                    matriz[filas][sub_indice] = matriz[filas][indice]
                    matriz[filas][indice] = auxiliar
    matriz_con_todos_los_heroes(matriz)


#Ejercicio 11)
def orden_alfabetico_descendete(matriz:list[list]) -> list:
    """Esta funcion ordena alfabeticamente descendete a los heroes segun su nombre

    Args:
    matriz (list[list]): Recibe la matriz con los heroes

    Returns:
    list: Devuelve la lista de heroes ordena alfabeticamente ascendente
    """
    cantidad_columnas = len(matriz[0])
    cantidad_filas = len(matriz)
    auxiliar = ""
    for indice in range (cantidad_columnas-1):
        for sub_indice in range(indice + 1,cantidad_columnas):
            if(matriz[2][indice] < matriz[2][sub_indice]):
                for filas in range(cantidad_filas):
                    auxiliar = matriz[filas][sub_indice]
                    matriz[filas][sub_indice] = matriz[filas][indice]
                    matriz[filas][indice] = auxiliar
    matriz_con_todos_los_heroes(matriz)


#ejercicio 12)
def orden_heroes_altura_asc_des(matriz:list[list])-> list:
    """Esta funcion ordena la altura de asc o desc

    Args:
        matiz (list[list]):Recibe la matriz con los heroes 

    Returns:
    list: Devuelve la lista ordenada dependiendo de lo que socilite el usuario
    """
    cantidad_columnas = len(matriz[0])
    cantidad_filas = len(matriz)
    auxiliares=""
    ingreso_usuario=input("Como quiere ordenar la altura de los heroes: [ASC/DESC]: ").upper()
    while ingreso_usuario !="ASC" and ingreso_usuario != "DESC":
        ingreso_usuario=input("ERORR.Como quiere ordenar la altura de los heroes: [ASC/DESC]: ").upper()    
    if ingreso_usuario == "ASC":
        for indice in range (cantidad_columnas-1):
            for sub_indice in range(indice + 1,cantidad_columnas):
                if(matriz[5][indice] > matriz[5][sub_indice]):
                    for filas in range(cantidad_filas):
                        auxiliar = matriz[filas][sub_indice]
                        matriz[filas][sub_indice] = matriz[filas][indice]
                        matriz[filas][indice] = auxiliar
        matriz_con_todos_los_heroes(matriz)    
    else:    
        for indice in range (cantidad_columnas-1):
            for sub_indice in range(indice + 1,cantidad_columnas):
                if(matriz[5][indice] < matriz[5][sub_indice]):
                    for filas in range(cantidad_filas):
                        auxiliar = matriz[filas][sub_indice]
                        matriz[filas][sub_indice] = matriz[filas][indice]
                        matriz[filas][indice] = auxiliar
        matriz_con_todos_los_heroes(matriz)

        





