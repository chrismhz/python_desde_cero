# Funcion simple
def calcula():
    calculo = 43 * 12 * 80
    calculo = calculo / 7
    coeficiente = 45 * 3.1416
    calculo = calculo * coeficiente
    calculo = "El resultado es: " + str(calculo)
    print(calculo)

# funcion recibe y devuelve parametros
def calcula_valor_2(numero1, numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    return suma, resta

res1, res2 = calcula_valor_2(10,100)

print(res1)
print(res2)
