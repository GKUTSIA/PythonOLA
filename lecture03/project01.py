def calculator ():
    while True:
        number_a = input("Enter 1st number: ")
        number_b = input("Enter 2nd number: ")
        operator = input("Choose the operation from the given operators (+, -, /, *): ")
        
        try:
            number_a = float(number_a)
            number_b = float(number_b)
        except ValueError:
            print("Error: could not convert string to float, try again!")

        if (operator == "+"):
            result = number_a + number_b
            print (f"a + b = {result}")
        
        # else:
        #     print ("Try again")
#        return 0


def guess_a_number ():
    print ("Try to guess")
    return 0


while True:
    print ("Choose the program")
    decision=input("1. Calculator\n2. Number Game\n3. Quit\n")
    if (decision == "q" or decision == "Q" or decision == "3" or decision == "quit"):
        print("Bye!\n\n")
        break
    elif (decision == "1"):
        calculator()
    elif (decision == "2"):
        guess_a_number()
    else:
        print ("Choose wisely!\n")