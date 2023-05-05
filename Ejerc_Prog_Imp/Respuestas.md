# Ejercicios Programacion Imperativa Python
## Objetivos
- Brindar ejercicios de apoyo y repaso utilizando este paradigma de programacion
- Desarrollar habilidades de interpretacion de enunciados bajo este paradigma
- Generar el espacio de interaccion y de correccion
- Posibilitar el entendimiento de nuevos paradigmas de desarrollo

## Ejercicios
1. Aspectos conceptuales
    - Las ventajas de utilizar funcione es de poder 'encerrar' codigo que cumpla una cierta funcion para poder ser reusado luego en otras partes de codigo sin tener que repetir ninguna linea de este.
    - Si al declarar la funcion se colocan los parametros de la manera *arg = val*, el orden no tiene importancia ya que se debera aclarar para cada valor a que parametro estamos haciendo referencia. En cualquier otro caso, el orden sí es importante y al llamar la funcion se debe seguir el orden de los parametros tal cual como estan en la declaracion de la funcion.
    - La sentencia *return* se utiliza para finalizar la funcion y que esta devuelva un objeto. Donde sea que la funcion llegue a un return, esta finalizará y dejara de ejecutarse.
    - La *definicion* de una funcion es donde nosotros la creamos y decidimos que parametros requiere y que funcion realizara con ellos. Por otro lado, la *invocacion* es cuando llamamos la funcion, le damos los parametros que pide y se ejecuta el cuerpo de la funcion con los parametro que nosotros le hallamos pasado.
    - Los parametro formales son variables locales dentro de la funcion, y permiten poder manipular los parametros de la funcion dentro de ella sin modificar las variables globales. Ejemplo ([Respuestas.py](/Ejerc_Prog_Imp/Respuestas.py))
    - Los parametros reales son los valores que se pasan a la funcion en la invocacion de la misma. Estos sirver para copiarse en los parametros formales y poder ejecutar el codigo de la funcion llamada. Ejemplo ([Respuestas.py](/Ejerc_Prog_Imp/Respuestas.py))
    - El cuerpo de la funcion es todo el codigo presente dentro de la funciony que se ejecutar en la invocacion de la misma. Ejemplo ([Respuestas.py](/Ejerc_Prog_Imp/Respuestas.py))
    - Si, existes funcion sin parametros. Esto se puede dar en casos donde la funcion no requiere ningun valor en especial que pueda varias, o tambien en funciones que trabajen unicamente con variables globales y/o ejecutan otras funciones.
    - Como parametro formal si es posible utilizar letras, pero no es posible utilizar numeros. Para los parametros reales es igual, pero no recomendable ya que dificultaria entender a que hace referencia el parametro.
    - Si, se puede tener una cantidad distinta de parametro formales y reales. Si la funcion pide 3 parametro, pero uno se instancia mas alla de si es pasado enla invocacion, cuando esta se haga solo se deberan pasar dos argumentos, pero dentro de la funcion habrá 3.
    - Para implementar un modulo con definiciones de funciones simplemente basta con crear un archivo .py donde se encuentren estas definiciones y luego desde otro archivos importalo. Esto es posible de varias maneras, entre ellas: *import [nombre]*, para importar todo el archivo; *from [nombre] import {funciones}*, para importar solo algunas de las funciones.
    - En *import math* se esta importando toda la libreria con todas sus funciones. Y para utilizarlas se tendria que invocar las funcion de la manera *math.[nombre_funcion]*. De la otra manera: *from math import sqrt*, se esta importando unicamente la funcion *sqrt* y se podra utilizar escribiendo *sqrt(num)*