num = int(input("Ingrese un número: "))

factorial = 1

for i in range(1, num):
    factorial = factorial * i 

print("El factorial de", num, "es:", factorial)