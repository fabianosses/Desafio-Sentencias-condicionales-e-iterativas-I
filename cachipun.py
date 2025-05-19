# importando librerías
import random
import sys

opciones = ["piedra", "papel", "tijera"]

# ingreso de argumentos (piedra, papel o tijera)
usuario = sys.argv[1]

print(f"elegiste {usuario}")

computador = random(opciones)

print(f"elegiste {computador}")