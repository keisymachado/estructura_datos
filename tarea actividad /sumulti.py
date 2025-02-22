def multiplicar(a, b):
    if b == 0:
        return 0
    if b > 0:  
        return a + multiplicar(a, b - 1)
    return -multiplicar(a, -b)

resultado = multiplicar(7, 3) 
print(resultado)