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


