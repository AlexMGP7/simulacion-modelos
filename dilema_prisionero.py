import random

def estrategia_prisionero():
    # Definimos las acciones posibles
    acciones = ['cooperar', 'traicionar']
    
    # Simulamos las decisiones de los prisioneros
    prisionero1 = random.choice(acciones)
    prisionero2 = random.choice(acciones)
    
    # Definimos los resultados del dilema
    if prisionero1 == 'traicionar' and prisionero2 == 'traicionar':
        return 'Ambos traicionan'
    elif prisionero1 == 'traicionar' and prisionero2 == 'cooperar':
        return 'Prisionero 1 traiciona y el 2 coopera'
    elif prisionero1 == 'cooperar' and prisionero2 == 'traicionar':
        return 'Prisionero 1 coopera y el 2 traiciona'
    else:
        return 'Ambos cooperan'

# Simulación de N rondas
def simular_rondas(num_rondas):
    resultados = {
        'Ambos traicionan': 0,
        'Prisionero 1 traiciona y el 2 coopera': 0,
        'Prisionero 1 coopera y el 2 traiciona': 0,
        'Ambos cooperan': 0
    }
    
    ultimas_rondas = []  # Lista para almacenar las últimas 10 rondas
    
    for ronda in range(num_rondas):
        resultado = estrategia_prisionero()
        resultados[resultado] += 1
        
        # Almacenar el resultado solo si estamos dentro de las últimas 10 rondas
        if ronda >= num_rondas - 10:
            ultimas_rondas.append(f"Ronda {ronda + 1}: {resultado}")
    
    # Calcular la probabilidad promedio de cada resultado
    print("Probabilidades promedio de cada resultado:\n")
    for resultado, conteo in resultados.items():
        probabilidad = conteo / num_rondas
        print(f"{resultado}: {probabilidad:.2%} probabilidad")
    
    # Mostrar las últimas 10 rondas
    print("\nResultados de las últimas 10 rondas:\n")
    for ronda in ultimas_rondas:
        print(ronda)

# Ejecutar la simulación con 10,000 rondas
simular_rondas(10000)
