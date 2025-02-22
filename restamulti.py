def division_por_sumas(dividendo, divisor):
    if divisor == 0:
        raise ValueError("No se puede dividir por cero")
    
    cociente = 0
    acumulador = abs(divisor)
    dividendo_absoluto = abs(dividendo)
    
    while acumulador <= dividendo_absoluto:
        acumulador += abs(divisor)
        cociente += 1
    
    if (dividendo < 0) ^ (divisor < 0): 
        cociente = -cociente
    
    return cociente