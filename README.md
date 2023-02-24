# Test cases cafetería

“Desarrolla una función para una cafetería "agregar nueva bebida". Una bebida se agrega como una sola línea String, no importa la Interfaz de Usuario en esta etapa, solo sabemos que una vez que se agrega una bebida pasa una String con las siguientes características: El nombre debe contener caracteres alfabéticos de 2 a 15 caracteres de longitud. El tamaño de la bebida, se puede ingresar un máximo de cinco tamaños para cada artículo, debe ser un valor en el rango de 1 a 48, solo números enteros. Los tamaños deben ingresarse en orden ascendente (primero los tamaños más pequeños). El nombre del artículo debe ingresarse primero, seguido de una coma, luego seguido de una lista de tamaños. Se utilizará una coma para separar cada tamaño. Los espacios (espacios en blanco) deben ignorarse en cualquier lugar de la entrada. Se requiere al menos un tamaño.

# Requisitos

Se requiere tener instalado Python3 y pip
Se requiere instalar pytest

    pip install pytest

## Cómo correr

    pytest

## Notas

Para verificar cada caso de prueba, se utiliza la función `assert()`, la cual verificar el return de la función `addNewDrink()` con el resultado esperado.
