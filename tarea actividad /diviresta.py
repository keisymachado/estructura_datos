def div (a:int,b: int)-> int:
    if a<b:
        return 0 
    return 1+div(a-b, b)

print (div(10,2))