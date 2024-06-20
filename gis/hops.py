import numpy as np


# Definición de la función para calcular el nivel de presión sonora
def calcular_presion_sonora(Lw, Q, q0, d, d0, Acor):
    """
    Calcula el nivel de presión sonora en un punto receptor.

    Parámetros:
    - Lw: Nivel de potencia sonora de la fuente estándar de tráfico (dB).
    - Q: Flujo de tráfico (vehículos/hora).
    - q0: Flujo de tráfico de referencia (vehículos/hora).
    - d: Distancia del receptor a la fuente de ruido (metros).
    - d0: Distancia de referencia (metros).
    - Acor: Correcciones por factores adicionales (dB).

    Retorna:
    - Lp: Nivel de presión sonora en el punto receptor (dB).
    """
    Lp = Lw + 10 * np.log10(Q / q0) - 20 * np.log10(d / d0) - Acor
    return Lp


# Ejemplo de uso:
Lw = 80  # Nivel de potencia sonora de una fuente estándar de tráfico en dB
Q = 1500  # Flujo de tráfico actual en vehículos/hora
q0 = 1000  # Flujo de tráfico de referencia en vehículos/hora
d = 50  # Distancia del receptor a la fuente de ruido en metros
d0 = 1  # Distancia de referencia en metros
Acor = 5  # Correcciones por factores adicionales en dB

# Calculo del nivel de presión sonora
Lp = calcular_presion_sonora(Lw, Q, q0, d, d0, Acor)
Lp
