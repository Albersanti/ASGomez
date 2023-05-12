##Simulemos un sistema donde se ingresan los precios de los productos comprados en un almacén.
#Cuando finaliza la compra le debemos preguntar como quiere pagar
#1 Efectivo
#2 3 cuotas sin interes
#3 12 cuotas con 10% de interes

#Si es Efectivo aplica la promocion del dia que es un descuento aleatorio entre el 15% y 25%

import random

precioTotal = 0  # Inicializamos el acumulador en cero

while True:  # Iteramos indefinidamente hasta que se ingrese un cero
    cantidad = float(input("Ingrese cantidad a pagar (Ingrese 0 para SALIR): "))
    if cantidad == 0:
        break  # Salimos del bucle si se ingresa un cero
    precioTotal += cantidad  # Sumamos la cantidad ingresada al acumulador


# Preguntamos al cliente cómo desea pagar
print("*** El precio total de los productos comprados es de:", precioTotal, "pesos. ***")
print("Por favor elija una forma de pago...")
print("1. Efectivo")
print("2. 3 cuotas sin interés")
print("3. 12 cuotas con 10 % de interés")

opcionPago = int(input("Ingrese el número de la opción elegida: "))

# Calculamos el descuento aleatorio si se eligió pagar en efectivo
if opcionPago == 1:
    descuento = random.randint(15, 25)
    totalCondescuento = precioTotal - (precioTotal * (descuento / 100))
    print(f"#### Al aplicarse un descuento del {descuento} %, el precio final a pagar en efectivo será de {round(totalCondescuento,2)} pesos. ####")
else:
    totalCondescuento = precioTotal

# Calculamos el precio final según la opción elegida
if opcionPago == 1:
    precioFinal1 = totalCondescuento   
elif opcionPago == 2:
    precioFinal2 = totalCondescuento / 3
    print(f"#### El precio final se abonará en 3 cuotas sin intereses de {round(precioFinal2,2)} pesos. ####")    
elif opcionPago == 3:
    precioFinal3 = totalCondescuento * 1.1 / 12

    print(f"#### El precio total se abonará en 12 cuotas de {round(precioFinal3,2)} pesos. ####")   

else:  
    print("*** La opción elegida es inválida. ")
