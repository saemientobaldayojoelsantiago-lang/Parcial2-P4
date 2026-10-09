
from collections import deque

def invertir_historial(historial):
    auxiliar = deque()
    invertida = []

    copia = historial.copy()

    while copia:
        auxiliar.append(copia.pop())

    while auxiliar:
        invertida.append(auxiliar.popleft())

    return invertida


historial = [
    "Solicitud recibida",
    "Repuesto asignado",
    "En reparación"
]

resultado = invertir_historial(historial)

print("Original:", historial)
print("Invertido:", resultado)
