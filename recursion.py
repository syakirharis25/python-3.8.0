def fibonacci(n):
    a, b = 0, 1
    for x in range(n):
        a, b = b, a+b
    return a

print(fibonacci(500))

def fibonacci2(n):
    if n <= 1:
        return n
    else:
        return (fibonacci2(n-1) + fibonacci2(n-2))

print(fibonacci2(500))
