#1)
from UTN_Heroes_Dataset.utn_matrices import matriz_data_heroes
from UTN_Heroes_Dataset.utn_funciones.auxiliares import color_text

cantidad_columnas = len(matriz_data_heroes[0])
cantidad_filas = len(matriz_data_heroes)

def validacion_de_tamaño(matriz,sub_indice,indice, espacio: int) -> str:
    texto = ""
    texto_saneado = ""
    texto_original = matriz[sub_indice][indice]
    if len(texto_original) >= espacio:
        texto_saneado = texto_original[0:espacio-1]
        texto += f"{texto_saneado:{espacio}} | "
    else: 
        texto += f"{texto_original:{espacio}} | "
    return texto
    
for indice in range(cantidad_columnas):
    texto = ""
    for sub_indice in range(cantidad_filas):

        match(matriz_data_heroes[sub_indice][indice]):
            case str():
                texto += f"{validacion_de_tamaño(matriz_data_heroes,sub_indice,indice,20)}"
            case int():
                texto += f"{matriz_data_heroes[sub_indice][indice]:03} | "
            case float():
                texto += f"{matriz_data_heroes[sub_indice][indice]:05.2f} | "
            case _:
                texto += f"{matriz_data_heroes[sub_indice][indice]} | "

    texto = texto[0:-3]
    print(texto) 