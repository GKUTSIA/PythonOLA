a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
greatest_divider = 1

for i in range(1,a+1):
    if ( a % i ==0 ) and ( b % i == 0 ):
        greatest_divider = i
print(greatest_divider)