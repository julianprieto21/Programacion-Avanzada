import time
from datetime import datetime
import random

# Decorador Timer
def timer(function):
    def wrapper():
        inicio = datetime.now().time()
        print(f"La funcion inició a las {inicio}")
        function()
        final = datetime.now().time()
        print(f"La funcion terminó a las {final}")
    return wrapper

@timer
def random_time():
    t = random.randint(1,5)
    print("Ejecutando...")
    print(f"La funcion tardará {t} segundos")
    time.sleep(t)

random_time()


# Decorador Timer con parámetros
def timer_switch(print_time = True):
    def timer2(function):
        def wrapper(*args, **kwargs):
            inicio = datetime.now().time()
            if print_time: print(f"La funcion inició a las {inicio}")
            function(print_time)
            final = datetime.now().time()
            if print_time: print(f"La funcion terminó a las {final}")
        return wrapper
    return timer2


@timer_switch(print_time = True)
def random_time_switch(print_time = True):
    t = random.randint(1,5)
    print("Ejecutando...")
    if print_time: print(f"La funcion tardará {t} segundos")
    time.sleep(t)

random_time_switch()


