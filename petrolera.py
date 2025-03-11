import numpy as np

def exploracion_petrolera(
    n_simulaciones=1000, 
    prob_exito=0.4,
    costo_exploracion=1_000_000, 
    barriles=300_000, 
    precio_barril=150,
    porcentaje_empresa=0.6
):
    """
    Realiza una simulación Monte Carlo para una exploración petrolera.
    
    Parámetros:
    -----------
    - n_simulaciones: número de veces que repetimos la exploración
    - prob_exito: probabilidad de encontrar petróleo (0.4 = 40%)
    - costo_exploracion: costo de cada exploración (1 millón USD)
    - barriles: barriles totales estimados si se encuentra petróleo
    - precio_barril: valor en USD de cada barril
    - porcentaje_empresa: qué porcentaje del valor de los barriles se queda la empresa (ej. 0.6 = 60%)
    
    Retorna:
    --------
    Un diccionario con resultados clave de la simulación: ganancias individuales, 
    total de éxitos, total de fracasos, ganancia promedio, desviación estándar y 
    umbral de éxito (proporción de éxitos sobre el total).
    """
    
    # Para almacenar las ganancias de cada simulación
    lista_ganancias = []
    
    # Contadores de éxito y fracaso
    exitos = 0
    
    # Simulación de Monte Carlo
    for _ in range(n_simulaciones):
        # Se determina si la exploración encuentra petróleo
        if np.random.rand() < prob_exito:
            # Si hay éxito, la empresa gana un 60% del valor de los barriles menos el costo
            ganancia = (barriles * precio_barril * porcentaje_empresa) - costo_exploracion
            exitos += 1
        else:
            # Si no se encuentra petróleo, se pierde el costo de exploración
            ganancia = -costo_exploracion
        
        lista_ganancias.append(ganancia)
    
    # Convertimos a numpy array para facilitar cálculos estadísticos
    ganancias_array = np.array(lista_ganancias)
    
    # Cálculos finales
    promedio_ganancias = ganancias_array.mean()
    desviacion_ganancias = ganancias_array.std()
    fracasos = n_simulaciones - exitos
    umbral_exito = exitos / n_simulaciones
    
    # Cálculos agregados
    ganancia_total_exitos = exitos * (barriles * precio_barril * porcentaje_empresa)
    perdida_total_fracasos = fracasos * costo_exploracion
    ganancia_total = ganancias_array.sum()
    
    # Mostrar reporte
    reporte = f"""
    ------------------ SIMULACIÓN EXPLORACIÓN PETROLERA ------------------
    Número de simulaciones: {n_simulaciones}
    - Éxitos (encuentran petróleo): {exitos}
    - Fracasos (no encuentran nada): {fracasos}
    
    Ganancia total (suma de todas las simulaciones): {ganancia_total:,.2f} USD
    Porcentaje de éxito (umbral de éxito): {umbral_exito:.2%}
    
    Ganancia promedio: {promedio_ganancias:,.2f} USD
    Desviación estándar: {desviacion_ganancias:,.2f} USD
    
    Ganancia agregada en los éxitos: {ganancia_total_exitos:,.2f} USD
    Pérdida agregada en los fracasos: {perdida_total_fracasos:,.2f} USD
    ----------------------------------------------------------------------
    """
    print(reporte)
    
    return {
        "ganancias_individuales": ganancias_array,
        "total_exitos": exitos,
        "total_fracasos": fracasos,
        "ganancia_promedio": promedio_ganancias,
        "desviacion_estandar": desviacion_ganancias,
        "umbral_exito": umbral_exito
    }

if __name__ == "__main__":
    resultados = exploracion_petrolera(n_simulaciones=1000)
    
    # --- Análisis de la estrategia ---
    # Cálculo teórico de la ganancia esperada (valor esperado)
    prob = 0.4
    costo = 1_000_000
    barr = 300_000
    valor = 150
    porc_emp = 0.6
    
    ganancia_si_exito = (barr * valor * porc_emp) - costo  # 60% de 300,000 barriles a 150 USD
    ganancia_esperada = prob * ganancia_si_exito + (1 - prob) * (-costo)
    
    print(f"Valor esperado teórico de una exploración: {ganancia_esperada:,.2f} USD")
    
    # Breakeven o probabilidad mínima de éxito para que la inversión sea rentable:

    p_breakeven = costo / (barr * valor * porc_emp)
    
    print(f"La probabilidad mínima para no perder dinero (breakeven) es: {p_breakeven:.2%}")
    
    # Conclusión de estrategia:
    # Si la probabilidad de encontrar petróleo (0.4 = 40%) es mayor que ~3.70% (p_breakeven),
    # la estrategia óptima es realizar la exploración.
    if prob > p_breakeven:
        print("Conclusión: Conviene explorar (la probabilidad de éxito supera el umbral de rentabilidad).")
    else:
        print("Conclusión: No conviene explorar (la probabilidad de éxito es demasiado baja).")
