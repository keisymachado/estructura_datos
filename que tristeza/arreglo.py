def sumaarreglo (reglo): 
    if not reglo :  
        return 0  
    return reglo [0]+ sumaarreglo (reglo[1:]) 

numeros =[1,2,3,4,5]
print (sumaarreglo(numeros))



