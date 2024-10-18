import random

# Función para lanzar la moneda y el dado
def lanzar_moneda_y_dado():
    moneda = random.choice(['cara', 'sello'])
    dado = random.randint(1, 6)
    return moneda, dado

# Función para determinar si se gana o se pierde
def es_ganador(moneda, dado):
    return moneda == 'cara' and dado % 2 == 0

# Simulación de 1000 tiradas
def simular_juego():
    saldo_inicial = 1000  # Saldo inicial
    saldo = saldo_inicial
    apuesta = 10  # Apuesta inicial
    tiradas = 100
    ganadas = 0
    perdidas = 0

    for i in range(tiradas):
        moneda, dado = lanzar_moneda_y_dado()
        if es_ganador(moneda, dado):
            saldo += apuesta * 2  # Gana el doble de lo apostado
            ganadas += 1
            apuesta = max(10, apuesta // 2)  # Si gana, apuesta la mitad o mínimo 10
        else:
            saldo -= apuesta  # Pierde la apuesta
            perdidas += 1
            apuesta *= 2  # Si pierde, duplica la apuesta

        # Si el saldo cae por debajo de 0, el jugador quiebra
        if saldo <= 0:
            print(f"El jugador ha perdido todo el dinero en la tirada {i + 1}.")
            break

    print(f"Después de {tiradas} tiradas:")
    print(f"Juegos ganados: {ganadas} ({ganadas / tiradas * 100:.2f}%)")
    print(f"Juegos perdidos: {perdidas} ({perdidas / tiradas * 100:.2f}%)")
    print(f"Saldo final: {saldo}")
    return ganadas / tiradas, perdidas / tiradas

# Ejecutar la simulación
probabilidad_ganar, probabilidad_perder = simular_juego()

# Verificar si se cumple la probabilidad de 25% de ganar y 75% de perder
if 0.24 <= probabilidad_ganar <= 0.26 and 0.74 <= probabilidad_perder <= 0.76:
    print("El resultado está dentro del rango esperado (25% ganar, 75% perder).")
else:
    print("El resultado no está dentro del rango esperado (25% ganar, 75% perder).")
