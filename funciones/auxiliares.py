from UTN_Heroes_Dataset.utn_funciones import (
    saludo, clear_console, play_sound
)

def limpiar_pantalla():
    """
    The function `limpiar_pantalla` clears the console screen and waits for user input to continue.
    """
    import os
    _ = input("\nPresiona Enter para continuar...")
    os.system('cls' if os.name in ['nt', 'dos'] else 'clear')
#
#from UTN_Heroes_Dataset.utn_matrices import matriz_data_heroes
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
#    for numero in matriz[4]:
#        if not minimo or minimo < numero:
#            minimo = numero
#    return float(minimo)
#
#if __name__ == "__main__":
#    obtener_poder_minimo(matriz_data_heroes)
#    