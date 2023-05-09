# 1) e.
# Ejemplo de parametros formales
a = 10
print(a) # 10
def mod_a(a):
    a = a + 1 # Parametro formal
    return a
mod_a(a)
print(a) # 10
# Como se ve, modificar el paramtro dentro de la funcion no me modifica el parametro real

# 1) f.
# Ejemplo de parametros reales
a = 10
print(a) # 10
def mod_a(a):
    a = a + 1
    return a
mod_a(a) # a: Parametro real
print(a) # 10

# 1) g.
# Ejemplo del cuerpo de una funcion
def mod_a(a):
    # Cuerpo de la funcion
    a = a + 1
    return a

# 2)
# I.
#   a.
# Dado el siguiente codigo indique cuales son los parametros formales y reales:

# Def de funciones
def sumaAlcuadrado(x, y):
    rta = x**2 + 2*x*y + y**2 # <- x e y son parametros formales aqui
    return rta
# Programa principal
print("Bienvenidos/as a la Suma al cuadrado")
# a = input("Ingrese el valor de a: ")
# b = input("Ingrese el valor de b: ")
# print(sumaAlcuadrado(a, b)) # <- a y b son parametros reales aqui
# Los parametro informales son x e y, y los parametros reales son a y b

#   b.
# Mencione los errores en los siguiente codigos y justifique:
# b.1.
# def suma(par1, par2):
#     print(par1+par2) # Error: No se retorna nada
# suma() # Error: No se le pasan parametros a la funcion
# b.2.
# def suma(par1, par2):
#     print(par1+par2) # Error: No se retorna nada
# print(suma(12, 10)) # Error: Se el print de la funcion y luego un None
# b.3.
# def suma(par1, par2):
#     return (par1+par2)
#     suma(12, 10) # Error: Se llama a la funcion dentro de la  misma funcion luego de que la funcion finalice con un return
# b.4.
# def suma(par1):
#     return (par1+2)
# suma(12, 10) # Error: Se le pasan 2 parametros a la funcion y solo debe recibir 1

# II.
def imprimir_mensaje():
    print("Estudiando Fundamentos de Informatica en la UNAB")
imprimir_mensaje()

# III.
def retorno_mensaje():
    return "Estudiando Fundamentos de Informatica en la UNAB"
# A. Para mostrar este mensaje basta con print(imprimir_mensaje())
# B. La diferencia es que en el primer caso se imprime el mensaje y en el segundo se retorna el mensaje
# C. Haria que se tenga que pasar el mensaje deseado como parametro a la funcion

# IV.
def imprimo_fecha(dia, mes, anio):
    print(f"{dia} de {mes} del {anio}")
imprimo_fecha(10, "Octubre", 2021)

# V.
def cuantos_dias(mes):
    if mes not in range(1, 13):
        return "Mes invalido"
    meses = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    return meses[mes]
print(cuantos_dias(1))

# VI.
def tabla_de(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")

# VII.
def area_circunferencia(radio, pi):
    return pi*radio**2
def area_rectangulo(lado_a, lado_b):
    return lado_a * lado_b
def area_cuadrado(lado):
    return lado*lado

# VIII
def calculo_rebaja(precio_prev, precio_sig):
    porcentaje = precio_sig * 100 / precio_prev
    return porcentaje


# IX
def calculo_nuevo_precio(precio_prev, porcentaje):
    resultado = porcentaje * precio_prev / 100
    return resultado

# X
def calculo_transporte(alumnos_1, alumnos_2, alumnos_3, asientos):
    alumnos = alumnos_1 + 3 + alumnos_2 + 3 + alumnos_3 + 3
    transportes = alumnpos / asientos
    return int(transportes + 1)

# XI 
def armo_cartel(producto, precio_prev, precio_sig):
    print("********************************")
    print("Atención!!! Gran rebaja para el producto nombre " + producto)
    print("Antes: precio anterio " + precio_prev)
    print("Ahora: precio rebajado " + precio_sig)

# XII
def calculo_litros(alto, ancho, profundidad):
    metros_cub = alto * ancho * profundidad
    litros = metros_cub * 1000
    return litros

# XIII
def a_pagar(cant_personas, monto_bebida, monto_comida, monto_alquiler):
    total = monto_bebida + monto_comida + monto_alquiler
    monto_unitario = total / cant_personas
    return monto_unitario

# XIV
def convertir_a_dolar(monto):
    res = monto / 470
    return round(res, 2)
def convertir_a_euro(monto):
    res = monto / 250
    return round(res, 2)
def convertir_a_real(monto):
    res = monto / 45
    return round(res, 2)

# Clases
class MontoPesos():
    def __init__(self, monto):
        self.monto = monto
        self.cotizacion = {"dolar": 470, "real": 45, "euro": 250}

    def actualizar_cotizaciones(self, moneda, cotizacion):
        self.cotizacion[moneda] = cotizacion

    def convertir(self, moneda):
        res = self.monto / self.cotizaciones[moneda]
        return round(res, 2)

    def a_dolar(self, cotizacion):
        res = self.monto / cotizacion
        return round(res, 2)
    def a_euro(self, cotizacion):
        res = self.monto / cotizacion
        return round(res, 2)
    def a_real(self, cotizacion):
        res = self.monto / cotizacion
        return round(res, 2)

monto = MontoPesos(100000)
# print(monto.a_dolar(470))
# print(monto.a_euro(250))
# print(monto.a_real(45))
# print(monto.a_dolar(100))
# print(monto.a_real(15000))
# print(monto.a_euro(10))
print(monto.convertir("dolar"))



# XV
def calculo_dosis(cant_dias, cant_veces, cant_comprimidos):
    total = cant_dias * cant_veces
    if total > cant_comprimidos:
        return False
    else: # total <= cant_comprimidos 
        return True

# XVI
def precio_con_iva(monto):
    return monto * 1.21

# XVII
def sumaPrimUlt(lista):
    prim = lista[0]
    ult = lista[-1]
    return prim + ult
def promedioPrimUlt(list):
    prim = lista[0]
    ult = lista[-1]
    total = prim + ult
    return total / 2
lista = [1, 1, 1]
lista[0] = int(input("Ingrese el primer valor: "))
lista[1] = int(input("Ingrese el segundo valor: "))
lista[2] = int(input("Ingrese el ultimo valor: "))
print(sumaPrimUlt(lista))
print(promedioPrimUlt(lista))

# XVIII
def cargarFraccion():
    num = int(input("Ingrese numerador: "))
    den = int(input("Ingrese denominador: "))
    lista = [num, den]
    return lista
def numeradorFraccion(x):
    return x[0]
def denominadorFraccion(x):
    return x[1]

def sumaFracciones(x, y)
    if x[1] == y[1]:
        z = [x[0] + y[0], x[1]]
        return z
    else:
        num = x[1] * y[0] + x[0] * y[1]
        den = x[1] * y[1]
        z = [num, den]
        return z

def restaFracciones(x, y):
    if denominadorFraccion(x) == denominadorFraccion(y):
        z = [numeradorFraccion(x) - numeradorFraccion(y), denominadorFraccion(x)]
        return z
    else:
        num = denominadorFraccion(x) * numeradorFraccion(y) - numeradorFraccion(x) * denominadorFraccion(y)
        den = denominadorFraccion(x) * denominadorFraccion(y)
        z = [num, den]
        return z

def divisionFracciones(x, y):
    num = numeradorFraccion(x) * denominadorFraccion(y)
    den = denominadorFraccion(x) * numeradorFraccion(y)
    return [num, den]

def multiplicacionFracciones(x, y):
    num = numeradorFraccion(x) * numeradorFraccion(y)
    den = denominadorFraccion(x) * denominadorFraccion(y)
    return [num, den]
print("Bienvenidos/as a cuentas con Fracciones")
a = cargarFraccion()
b = cargarFraccion()
print("El denominador de la primera fraccion es: " + denominadorFraccion(a))
print("El numerador de la segunda fraccion es:" + numeradorFraccion(b))
print("La suma de dichas fracciones es:" + sumaFracciones(a, b))
print("La resta de dichas fracciones es:" + restaFracciones(a, b))
print("La multiplicacion de dichas fracciones es:" + multiplicacionFracciones(a, b))
print("La division es:" + divisionFracciones(a, b))
# Clases
class Fraccion():
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
        self.fraccion = [numerador, denominador]
    def sumar(self, other):
        if self.denominador == other.denominador:
            num = self.numerador + other.numerador
            fraccion_nueva = [num, self.denominador]
            return fraccion_nueva
        else:




