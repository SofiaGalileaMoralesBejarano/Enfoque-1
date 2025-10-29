# Enfoque 1: Teoria de la utilidad funcion de utilidad
# Autor: Sofia Galilea Morales Bejarano 6°E

# Objetivo: 
# Este código calcula la utilidad de decisiones de varias personas, 
# aplicando una función de utilidad que convierte el valor de cada decisión en un puntaje comparables entre sí.

# Inicio:

def calcular_utilidad(decision, valor):
    # Calcula la utilidad multiplicando el valor de la decisión por 10
    return valor * 10   

# Definición de decisiones de varias personas con un valor asociado
decisiones = {
    "Jose": {"decisión": "Invertir", "valor": 8},  
    "Juan": {"decisión": "Ahorrar", "valor": 6},  
    "Angel": {"decisión": "Gastar", "valor": 5}      
}

# Recorro cada decisión, calculo su utilidad y la muestro
for nombre, info in decisiones.items():
    decision = info["decisión"]
    valor = info["valor"]
    utilidad = calcular_utilidad(decision, valor)  # Calculo la utilidad
    print(f"{nombre} tomó la decisión de {decision} con una utilidad de {utilidad}.")
