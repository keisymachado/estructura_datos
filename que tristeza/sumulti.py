def multiplicar(a, b):
    if b == 0:
        return 0
    if b < 0:  
        return a + multiplicar(a, b - 1)
resultado = multiplicar(0, 3) 
print(resultado)