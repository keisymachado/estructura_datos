def fibonacci(n:int)-> int:
    if n <= 1:
        return n
    return fibonacci (n-1) + fibonacci(n-2)
for i in range(8):
    print(fibonacci(i))