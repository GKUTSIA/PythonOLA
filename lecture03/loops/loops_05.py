y = 0

for x in range(1500,2101):
    if ( x % 35 == 0 ):
        y = y + x
        if ( y > 20000 ):
            break
    
print(y)