
from collections import deque

def eliminar_canceladas(cola):
    auxiliar = deque()

    for solicitud in cola:
        if solicitud["estado"] != "Cancelada":
            auxiliar.append(solicitud)

    return auxiliar


cola = deque([
    {"id": 1, "estado": "Pendiente"},
    {"id": 2, "estado": "Cancelada"},
    {"id": 3, "estado": "En atención"},
    {"id": 4, "estado": "Pendiente"}
])

cola = eliminar_canceladas(cola)

for solicitud in cola:
    print(solicitud)
