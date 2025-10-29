Enfoque 1: Salto atras dirigido por conflictos
# Autor: Sofia Galilea Morales Bejarano 6°E

# Objetivo:

# Este código usa backtracking para resolver un problema de asignación de colores, 
# asignando un color distinto a cada persona y retrocediendo cuando ocurre un conflicto hasta encontrar una solución válida.

def salto_atras_conflictos(nombres, colores):
    asignacion = {nombre: None for nombre in nombres}  # Inicializo sin asignar colores

    def es_valido(nombre, color):
        # Verifico que ningún otro ya tenga el mismo color
        for n, c in asignacion.items():
            if n != nombre and c == color:  
                return False
        return True  

    def asignar_colores(i):
        # Si ya asigné colores a todos, retorno True
        if i == len(nombres):
            print("Asignación completa y válida:", asignacion)
            return True
        
        nombre_actual = nombres[i]  
        for color in colores:
            if es_valido(nombre_actual, color):
                asignacion[nombre_actual] = color  # Asigno temporalmente
                print(f"Asignando {color} a {nombre_actual}")

                # Intento continuar con la siguiente persona
                if asignar_colores(i + 1):
                    return True 
                
                # Retrocedo si la asignación no lleva a solución
                print(f"Retrocediendo, quitando asignación de {nombre_actual}")
                asignacion[nombre_actual] = None
        
        # Si no hay color válido para esta persona, retorno False
        return False 

nombres = ["Fernanda", "Emmanuel", "Carlos"]
colores = ["Rojo", "Verde", "Azul"]

# Inicio la búsqueda de asignaciones válidas
if not salto_atras_conflictos(nombres, colores):
    print("No se encontró una asignación válida.")
