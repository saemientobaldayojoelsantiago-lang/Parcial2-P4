
def registrar_accion(pila, accion):
    if len(pila) == 5:
        pila.pop(0)

    pila.append(accion)


historial = [
    "Crear solicitud",
    "Registrar vehículo",
    "Asignar repuesto",
    "Cambiar estado",
    "Asignar técnico"
]

registrar_accion(historial, "Despachar vehículo")

print(historial)
