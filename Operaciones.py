
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
