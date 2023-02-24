# Instructions
# El nombre debe contener caracteres alfabéticos de 2 a 15 caracteres de longitud. 
# El tamaño de la bebida, se puede ingresar un máximo de cinco tamaños para cada artículo, 
# debe ser un valor en el rango de 1 a 48, solo números enteros. Los tamaños deben ingresarse 
# en orden ascendente (primero los tamaños más pequeños). 
# El nombre del artículo debe ingresarse primero, seguido de una coma, luego seguido de una lista de tamaños. 
# Se utilizará una coma para separar cada tamaño. Los espacios (espacios en blanco) 
# deben ignorarse en cualquier lugar de la entrada. Se requiere al menos un tamaño.


def addNewDrink(str):

    if str=="":
        return "No input"
    
    listStr = str.split(",")
    drinkName = listStr[0]

    if not drinkName.isalpha():
        return "Error in name of the drink. Contains character no alpha"
    
    if len(drinkName) < 2:
        return "Error in name of the drink. Too short"

    if len(drinkName) > 15:
        return "Error in name of the drink. Too large"
    
    if len(listStr) == 1:
        return "Error in the number of drink sizes. No sizes"

    if len(listStr) > 6:
        return "Error in the number of drink sizes. Too many"
    
    # Loop sizes to check if are float or drink drink sizes
    for i in range(1, len(listStr)):

        # check for float
        drinkSize = listStr[i].strip()
        if drinkSize.replace('.', '', 1).isdigit() and not float(drinkSize).is_integer():
            return "Error in the drink sizes. Contains float values"
        
        # Check for string
        try:
            drinkSizeNum = int(drinkSize)
        except ValueError:
            return "Error in the drink sizes. Contains string values"
        
    
    # Loop for negative values, zero values, and greather than 48 values
    for i in range(1, len(listStr)):
        if int(listStr[i]) < 0:
            return "Error in drink sizes. No negative values accepted"
        if int(listStr[i]) == 0:
            return "Error in drink sizes. Drink size can't be zero"
        if int(listStr[i]) > 48:
            return "Error in drink sizes. No drink sizes greather than 48 are accepted"
        

    # Loop sizes to check if they are in ascenendt order
    prevSize = 0
    for i in range(1, len(listStr)):
        if prevSize > int(listStr[i]) or int(listStr[i]) >= 48:
            return "Error in drink sizes. No ascending order"
        prevSize = int(listStr[i])


    return "Successful insertion"


# Test cases

def test_no_input():
    assert addNewDrink("") == "No input"

def test_error_drink_name():
    assert addNewDrink("Michelada23, 4, 5, 6") == "Error in name of the drink. Contains character no alpha"
    
def test_error_drink_name2():
    assert addNewDrink("4, 5, 6") == "Error in name of the drink. Contains character no alpha"

def test_error_drink_name3():
    assert addNewDrink(" , 4, 5, 6") == "Error in name of the drink. Contains character no alpha"

def test_error_drink_name_too_short():
    assert addNewDrink("M, 4, 5, 6") == "Error in name of the drink. Too short"

def test_error_drink_name_too_large():
    assert addNewDrink("MiSuperBebidaMajestuosa, 4, 5, 6") == "Error in name of the drink. Too large"

def test_error_too_many_sizes():
    assert addNewDrink("Vampiro, 4, 5, 6, 7, 8, 9") == "Error in the number of drink sizes. Too many"

def test_error_no_sizes():
    assert addNewDrink("Vampiro") == "Error in the number of drink sizes. No sizes"

def test_sizes_contain_float():
    assert addNewDrink("Pitufo, 5, 10, 15.3, 20.4, 25") == "Error in the drink sizes. Contains float values"

def test_sizes_contain_float2():
    assert addNewDrink("Pitufo, 5.2, 25") == "Error in the drink sizes. Contains float values"

def test_sizes_contain_string():
    assert addNewDrink("Pitufo, 5, 10, Eleven11") == "Error in the drink sizes. Contains string values"

def test_sizes_contain_string2():
    assert addNewDrink("Coca, cola, 5, 10, Eleven11") == "Error in the drink sizes. Contains string values"

def test_sizes_contains_zero():
    assert addNewDrink("Pitufo, 0, 5, 10, 20, 30") == "Error in drink sizes. Drink size can't be zero"

def test_sizes_contains_negatives():
    assert addNewDrink("Pitufo, -3, 5, 10, 20, 30") == "Error in drink sizes. No negative values accepted"

def test_sizes_contains_greater():
    assert addNewDrink("Pitufo, 5, 10, 20, 50") == "Error in drink sizes. No drink sizes greather than 48 are accepted"

def test_error_ascending_order():
    assert addNewDrink("Vampiro, 4, 5, 10, 3") == "Error in drink sizes. No ascending order"

def test_succes():
    assert addNewDrink("Pitufo, 5, 10, 15, 20, 25") == "Successful insertion"

def test_succes2():
    assert addNewDrink("Pitufo, 5 ") == "Successful insertion"

def test_succes2():
    assert addNewDrink("Pitufo, 5, 17 ") == "Successful insertion"


