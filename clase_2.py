class CuentaBancaria():
    ''' Clase que nos permite la gestión de una Cuenta Bancaria genérica!
    '''
    
    def __init__(self, saldo_inicial, nombre, apellido, moneda = '$'):
        # TODO: Ver la forma de soportar cajas de ahorro y/o cuentas corrientes
        self.tipo_cuenta = None
        self.movimientos = []
        self.saldo = saldo_inicial
        self.nombre = nombre
        self.apellido = apellido
        self.moneda = moneda

    # Se agregó los metodos de verificar_saldo, y pagar
    # def verificar_saldo(monto):
    #     if self.saldo < monto:
    #         return false
    #     else:
    #         return true

    # def pagar(monto, other):
    #     if self.verificar_saldo(monto):
    #         other.saldo += monto
    #         self.saldo -= monto
    #         self.movimientos.append(f"Transaccion de {self.moneda+monto} a {other.nombre} {other.apellido}")            
    #         return "Transaccion realizada"
    #     else:
    #         return "Saldo Insuficiente para realizar la transaccion"

    def depositar(self, monto):
        '''Método que nos permite realizar un depósito bancario'''
        self.movimientos.append('DEPOSITO: ' + str(monto))
        self.saldo = self.saldo + monto


    def extraer(self, monto):
        '''Método que nos permite realizar una extracción de un cuenta bancaria'''
        if self.saldo - monto >= 0:
            self.movimientos.append('EXTRACCION: ' + str(monto))
            self.saldo = self.saldo - monto
        else:
           self.movimientos.append('SALDO INSUFICIENTE: ' + str(monto)) 
           print("Saldo insuficiente")
        

    def datos_titular(self):
        '''Método que nos permite mostrar los datos del titular y su saldo'''
        return self.apellido + ', ' + self.nombre + " con el saldo: " + str(self.saldo) + " " + self.moneda
    
    def datos_saldo(self):
        return self.saldo

    def _reset_saldo(self):
        self.saldo = 0 

    def datos_movimientos(self):
        return list(self.movimientos)

class Cuenta_Corriente(CuentaBancaria):
    def __init__(self, saldo_inicial, nombre, apellido, limite_descubierto, moneda = '$'):
        super().__init__(saldo_inicial, nombre, apellido, movimientos, moneda)
        self.limite_descubierto = limite_descubierto
        self.tipo_cuenta = "CC"

    def extraer(self, monto):
        '''Método que nos permite realizar una extracción de un cuenta bancaria'''
        if self.saldo - monto >= 0:
            self.movimientos.append('EXTRACCION: ' + str(monto))
            self.saldo = self.saldo - monto
        else:
            if self.saldo - monto <= self.limite_descubierto:
                self.movimientos.append('EXTRACCION: ' + str(monto))
                self.saldo = self.saldo - monto
            else:
                self.movimientos.append('SALDO INSUFICIENTE: ' + str(monto)) 
                print("Saldo insuficiente")
        

    def datos_titular(self):
        return f"{self.apellido}, {self.nombre} con el saldo: {self.saldo} {self.moneda}. Tipo de cuenta: {self.tipo_cuenta} con un limite descubierto de {self.limite_descubierto}"


class Caja_de_Ahorro(CuentaBancaria):
    def __init__(self, saldo_inicial, nombre, apellido, moneda = '$'):
        super().__init__(saldo_inicial, nombre, apellido, movimientos, moneda)
        self.tipo_cuenta = "CA"
    



from Math import pi

class Figura:
    pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado 

    def perimetro(self):
        return self.lado * 4

class Rectangulo(Figura):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1 
        self.lado2 = lado2 

    def perimetro(self):
        return 2*self.lado1 + 2*self.lado2

# TODO: Pensar en otra posible herencia (taxonomía)
class Circunferencia(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def perimetro(self):
        return 2*pi*self.radio

    def area(self):
        return pi*self.radio**2


# Pruebas
c1 = Cuadrado(6)
c2 = Cuadrado(4)
print(c1.perimetro())
print(c2.perimetro())

r1 = Rectangulo(3,4)
r2 = Rectangulo(4,10)
print(r1.perimetro())
print(r2.perimetro())

cir1 = Circunferencia(10)
cir2 = Circunferencia(5)
print(cir1.area())
print(cir2.perimetro())
