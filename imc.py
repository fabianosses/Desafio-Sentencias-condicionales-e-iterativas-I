# importando librerías
import sys

# ingreso de datos
w = float(sys.argv[1])
h = float(sys.argv[2])

# calculo de IMC
h = h/100
imc = w / ( h ** 2)

# imprimir resultado de IMC
print(f"Su IMC es  : {imc:.2f}")

# condicionantes clasificación grado de obesidad
if imc < 18.5 :
  print ("La clasificación OMS es Bajo Peso")

elif imc > 18.5 and imc <= 25:
  print ("La clasificación OMS es Adecuado")

elif imc > 25 and imc <= 30:
  print ("La clasificación OMS es Sobrepeso")

elif imc > 30 and imc <= 35:
  print ("La clasificación OMS es Obesidad Grado I")

elif imc > 35 and imc <= 40:
  print ("La clasificación OMS es Obesidad Grado II")

else:
  print ("La clasificación OMS es Obesidad Grado III")