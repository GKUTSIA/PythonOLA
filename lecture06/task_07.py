text = ""
print("Enter the text:\n")

while True:
    char = input()
    if char == '0':
        break
    else:
        with open('data.txt', 'a', encoding = 'utf-8') as f1:
            f1.write(char + "\n")
    


