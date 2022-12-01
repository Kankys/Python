# && = A zároveň
# || = nebo

# Zákldaní příklad:
a = int(input("Zadejte číslo v rozmezí 10-20: "))
if a >= 10 and a <= 20:
    print("Zadal jsi správně")
else:
    print("Zadal jsi špatně")    
    
# Pomocí závorek můžeme operátory kombinovat:

a = int(input("Zadejte číslo v rozmezí 10-20 nebo 30-40: "))    
if (a >= 10 and a <= 20 ) or (a >= 30 and a <= 40 ):
    print("Zadal jsi správně")
else:
    print("Zadal jsi špatně") 