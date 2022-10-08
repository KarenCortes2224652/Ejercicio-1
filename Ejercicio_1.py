# Ejercicio 1:
print("--------------------------------------")
print("--- CALCULAR - SUMA - DE - DIGITOS ---")
print("--------------------------------------")

#Input
n = int(input("Ingresa un número entero y positivo :"))
m = n

#Processing
if n != 0:
    suma = 0
    while n > 0:
        suma = suma + n % 10
        n = n // 10
    print("La suma de", m, "es:", suma)
else:
    print("El número ingresado debe ser entero y positivo")
        

