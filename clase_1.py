# Crear funciones para calcular area y perimetro
# de un cuadrado, de un rectangulo y de una circunferencia

def area_cuadrado(lado):
    return lado*lado

def perimetro_cuadrado(lado):
    return lado*4

def area_rectangulo(lado_a, lado_b):
    return lado_a * lado_b

def perimetro_rectangulo(lado_a, lado_b):
    return lado_a*2 + lado_b*2

def area_circunferencia(radio):
    return 3.14*radio**2

def perimetro_circunferencia(radio):
    return 2*3.14*radio

# Test
print(area_cuadrado(10))
print(perimetro_cuadrado(10))
print(area_rectangulo(5, 2))
print(area_rectangulo(5, 2))
print(area_circunferencia(12))
print(area_circunferencia(12))

