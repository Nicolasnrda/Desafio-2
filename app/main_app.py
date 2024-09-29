from UTN_Heroes_Dataset.utn_matrices import matriz_data_heroes
from funciones import (
    mostrar_menu, matriz_con_todos_los_heroes, mostrar_por_genero, mas_de_setentaycinco_en_poder, mas_de_cientosesenta_de_altura
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
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                pass
            case 10:
                pass
            case 11:
                pass
            case 12:
                pass
            case 13:
                break
        limpiar_pantalla()
