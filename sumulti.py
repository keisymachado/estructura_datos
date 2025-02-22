def multiplicar(a, b):
    resultado = 0
    for _ in range(b): 
        resultado += a  
    return resultado

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
print("(", num1, ") x (", num2, ") = (", multiplicar(num1, num2), ")")