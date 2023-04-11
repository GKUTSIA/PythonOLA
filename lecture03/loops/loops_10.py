factorial = 1
x = int(input("Enter the number: "))

while ( x > 0 ):
    factorial = factorial * x
    x -= 1
    
print(factorial)