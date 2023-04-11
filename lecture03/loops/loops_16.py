x = int(input("Enter the number: "))
counter = 0

for i in range(1,x+1):
    if ( x % i ) == 0:
        print(i)
        counter += 1

if (counter > 2):
    print("Number is not simple")
else:
    print("Number is simple")
    