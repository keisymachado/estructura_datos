def dividir(a, b)->float:
    if b == 0:
     return "Error: imposible dividir por cero cacorro"
    cociente = 0
    while a >= b:
        a = a-b
        cociente =cociente+ 1
    return cociente + a / b
print("Ingresa el valor a dividir: ")
a = int(input())
print("Ingresa el otro valor : ")
b = int(input())

print("El cociente es:",round(dividir(a, b), 3))