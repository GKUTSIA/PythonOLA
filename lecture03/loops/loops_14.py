a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
least_common_multiple = 1
greatest_divider = 1


for i in range(1,a+1):
    if ( a % i ==0 ) and ( b % i == 0 ):
        greatest_divider = i
least_common_multiple = ( a * b ) / greatest_divider
print(least_common_multiple)