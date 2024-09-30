from UTN_Heroes_Dataset.utn_matrices import matriz_data_heroes
from funciones import (
    mostrar_menu, matriz_con_todos_los_heroes, mostrar_por_genero, mas_de_setentaycinco_en_poder, 
    mas_de_cientosesenta_de_altura,femenino_mas_60,masculino_menos_60, heroes_con_poder_menor,
    heroes_con_maximo_altura, orden_alfabetico_ascendente
)
from funciones import (
    play_sound, limpiar_pantalla
)
from validaciones import validar_opcion

def utn_heroes(matriz_data_heroes):
    while True:
        mostrar_menu()
        opcion = validar_opcion(1, 13)
        play_sound()
        match opcion:
            case 1:
                mostrar_por_genero(matriz_data_heroes, "Femenino")
            case 2:
                mostrar_por_genero(matriz_data_heroes, "Masculino")
            case 3:
                mas_de_setentaycinco_en_poder(matriz_data_heroes)
            case 4:
                mas_de_cientosesenta_de_altura(matriz_data_heroes)
            case 5:
                femenino_mas_60(matriz_data_heroes, "Femenino")
            case 6:
                masculino_menos_60(matriz_data_heroes,"Masculino")
            case 7:
                pass
            case 8:
                heroes_con_poder_menor(matriz_data_heroes)
            case 9:
                heroes_con_maximo_altura(matriz_data_heroes)
            case 10:
                orden_alfabetico_ascendente(matriz_data_heroes)
            case 11:
                pass
            case 12:
                pass
            case 13:
                break
        limpiar_pantalla()
