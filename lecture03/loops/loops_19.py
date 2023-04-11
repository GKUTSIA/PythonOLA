x = int(input("Enter the number: "))

digits = 0

while (x > 0):
    digits += 1
    x = round(x / 10)

print(digits)