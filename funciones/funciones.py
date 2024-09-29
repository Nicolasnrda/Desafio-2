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
            




