# დაწერეთ პროგრამა, რომლის მეშვეობითაც შეიტანთ 3 რიცხვს. იპოვეთ ამ რიცხვებს
# შორის მინიმუმი და დაბეჭდეთ ეკრანზე (გამოიყენეთ if ოპერატორი).

num_a = int(input("Please enter first number: "))
num_b = int(input("Please enter second number: "))
num_c = int(input("Please enter third number: "))

if ( (num_a < num_b) and (num_a < num_c) ):
    print (num_a, "is the smallest")

if ( (num_a > num_b) and (num_b < num_c) ):
    print (num_b, "is the smallest")

if ( (num_a > num_c) and ( num_b > num_c ) ):
    print (num_c, "is the smallest")


