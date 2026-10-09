# Parcial2-P4

# Punto uno:
Cómo explicarlo:

Copio el historial para no modificar el original.

Extraigo los elementos de la pila con pop() y los introduzco en la cola con append().

Extraigo los elementos de la cola con popleft() y los introduzco en la nueva pila.

Devuelvo la pila invertida.

La cola es la estructura intermedia que permite invertir el orden.

# Punto 2:

Cómo explicarlo:

Creo una cola auxiliar vacía.

Recorro las solicitudes en su orden de llegada.

Si una solicitud está cancelada, no la agrego.

Si no está cancelada, la agrego a la cola auxiliar.

Devuelvo la nueva cola con las solicitudes válidas.

Se conserva el orden FIFO (First In, First Out): la primera solicitud que llega sigue siendo la primera en la cola. La cola original no se modifica durante el filtrado.


# Punto 3:

Cómo explicarlo:

La función recibe la pila y la nueva acción.

len(pila) cuenta cuántas acciones hay.

Si hay cinco, pop(0) elimina la acción más antigua, que está en el fondo.

append(accion) agrega la nueva acción al tope.

La pila termina con un máximo de cinco elementos.

Importante: en esta implementación, el fondo de la pila está en la posición 0 y el tope está al final de la lista.
