# დაწერეთ პროგრამა, სადაც შეიტანთ (input) ნებისმიერ რიცხვს 0-დან 100-ის ჩათვლით
# და შედეგად გამოიტანს შეფასების შესაბამის ლათინურ დასახელებას შემდეგი სქემის
# მიხედვით. მაგ. თუ შეიტანთ 45-ს, პროგრამამ უნდა დაბეჭდოს FX.

# ქულა შეფასება
# 91-100 A
# 81-90 B
# 71-80 C
# 61-70 D
# 51-60 E
# 41-50 FX
# 0-40 Failed

score = int(input("Enter Score: "))

if ( score > 90 ):
    print ("A")
elif ( score > 80 ):
    print ("B")
elif ( score > 70 ):
    print ("C")
elif ( score > 60 ):
    print ("D")
elif ( score > 50 ):
    print ("E")
elif ( score > 40 ):
    print ("FX")
else:
    print ("Failed")