
# Operaciones con Python

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b    

def Multi(a, b):
    return a*b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "No se puede dividir por cero"

# Pruebas
if __name__ == "__main__":
    print(suma(5, 3))
    print(resta(5, 3))
    print(Multi(5, 3))
    print(division(5, 3))
    print(division(5, 0))