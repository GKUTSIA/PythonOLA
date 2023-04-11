biggest_num = 0

for i in range(0,10):
    a = int(input("Enter the number: "))
    if ( a % 2 == 1 ) and ( a > biggest_num ):
        biggest_num = a        


if ( biggest_num == 0 ):
    print("Odd number not found")
else:
    print(biggest_num)