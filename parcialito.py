def promedio(list):
    suma = 0
    for val in lista:
        suma += val
    prom = suma / len(lista)
    return prom

lista = [1, 2, 3]
print(promedio(lista))

def es_par(num):
    if num % 2 == 0:
        return True
    else:
        return False

num = 5
print(es_par(num))

def factorial(num):
    # i = 1
    # res = 1
    # for n in range(num):
    #     res *= i
    #     i += 1
    # return res
    f = 1
    for x in range(1, n+1):
        f *= x
    return f

print(factorial(num))

def pares(lista):
    res = []
    for val in lista:
        if val % 2 == 0:
            res.append(val)
    return res

print(pares(lista))

def sum_pares(par1, par2):
    res = (par1[0] + par2[0], par1[1] + par2[1])
    return res

print(sum_pares([2, 6], [1, 2]))
