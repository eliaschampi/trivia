#las importaciones al principio
import time


#AQUI AGREGAMOS LA CLASE COLOR CON COLORES COMO PROPIEDAD
class color:
    ROSA = '\033[95m'
    CYAN = '\033[96m'
    CYANOSCURO = '\033[36m'
    AZUL = '\033[94m'
    VERDE = '\033[92m'
    AMARILLO = '\033[93m'
    ROJO = '\033[91m'
    NEGRITA = '\033[1m'
    LINEA = '\033[4m'
    FIN = '\033[0m'


#ESTABLECEMOS PREMIO POR DEFECTO
PREMIO = "Una entrada al cine"
MAXIMO_INTENTOS = 3


#mis funciones
def muestraMisLineas():
    print(color.ROSA, "-----------------------", color.FIN)


def muestraMiLoading(cuanto):
    contador = 0
    print(color.CYAN)
    while contador < cuanto:
        contador = contador + 1
        time.sleep(0.5)
        print(" * ", end='')
    print(color.FIN)


def muestraLaAyuda():
    print(
        color.AMARILLO,
        "Piedra papel o tijera\n Es un juego para una decisión rapida entre dos personas."
    )
    print("Debes ingresar una de estas tres opciones:")
    print("1 va a ser piedra.")
    print("2 va a ser papel.")
    print("3 va a ser tijera.", color.FIN)


def configuraElPremio():
    print(color.AMARILLO, "Selecciona un premio:")
    premios = {
        "c": "Un cafecito",
        "p": "Una pizza",
        "m": "Una entrada al cine"
    }
    print("c: Un cafecito")
    print("p: Una pizza")
    print("m: Una entrada al cine", color.FIN)
    opcionPremio = input("Ingresa una opcion:")
    intentosopcion = 0
    while opcionPremio not in ["c", "p", "m"
                               ] or intentosopcion <= MAXIMO_INTENTOS:
        intentosopcion = intentosopcion + 1
        opcionPremio = input("Opcion incorrecta, Ingresa c, p o m:")
    PREMIO = premios[opcionPremio]


#INICIO DEL PROGRAMA
#Aqui mostramos en la pantalla el texto de bienvenida
print(color.NEGRITA, "Hola! Bienvenido a mi trivia")
#llamamos nuestra funcion aqui
muestraMisLineas()
#Obtenemos el nombre aqui
name = input("¿Me podrías decir como quieres que te llame?\nIngresa Aqui:")

#Damos bienvenida
print(color.VERDE,
      "Bienvenido " + name + ", Ahora vamos a jugar piedra papel o tijeras",
      color.FIN)

#carga el juego!!!
muestraMiLoading(15)

#MENU DEL JUEGO
print(color.NEGRITA, "MENU DEL JUEGO:")
muestraMisLineas()
print("a: Mostrar ayuda")
print("c: Configurar premio")
print("p: Jugar ahora")
print("s: Salir del juego")
opcionPrincipal = input("Ingresa una opción:") or "p"

#VALIDAMOS
while opcionPrincipal not in ["a", "c", "p"]:
    opcionPrincipal = input("Opcion incorrecta, ingresa nuevamente:") or "p"

if opcionPrincipal == "a":
    muestraLaAyuda()
elif opcionPrincipal == "c":
    configuraElPremio()
