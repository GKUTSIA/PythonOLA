# დაწერეთ პროგრამა, რომლის მეშვეობითაც შეიტანთ ნებისმიერ რიცხვს. პროგრამამ
# შეამოწმოს, თუ რიცხვი დადებითია, დაბეჭდოს ეკრანზე “Number is positive”, თუ რიცხვი
# უარყოფითია, დაბეჭდოს “Number is negative”, თუ არადა დაბეჭდოს “Number is equal to zero”.

x = int(input("Please enter the number: "))

if ( x == 0 ):
    print ("Number is equal to zero")
elif ( x > 0 ):
    print ("Number is positive")
else:
    print ("Number is negative")
