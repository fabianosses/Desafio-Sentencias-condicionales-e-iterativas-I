# importando librerías
import random
import sys

# define argumentos que deben elegir al azar
argumentos = ["piedra", "papel", "tijera"]

# ingreso de argumentos (piedra, papel o tijera)
usuario = sys.argv[1]

# Loops
while True:

    print(f"elegiste: {usuario}")

    if usuario == "salir":
        print("¡FIN!")
        break

    if usuario not in argumentos:
        usuario = input("""Argumento no válido ... 
                        elige: piedra, papel o tijera.
                        o escribe "salir" para finalizar """)
        continue

    computador = random.choice(argumentos)
    print(f"computador: {computador}")

    if usuario == computador :
        print("empate!!!...")

    elif (usuario == "piedra" and computador == "tijera") or \
        (usuario == "papel" and computador == "piedra") or \
        (usuario == "tijera" and computador == "papel"):
        usuario = input(""" Ganaste!!!... 
                        elige: piedra, papel o tijera.
                        o escribe "salir" para finalizar """)
    else:
        usuario = input("""Perdiste!!! :( 
                        elige: piedra, papel o tijera.
                        o escribe "salir" para finalizar """)