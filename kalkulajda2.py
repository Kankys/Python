# Použití příkazu elif z příkazů else-if

print("Vítej v kalkulajdě!")
a = float(input("Zadej první číslo:"))
b = float(input("Zadej druhé číslo:"))
print("vyber jednu z možností:")
print("1 - sčítání")
print("2 - odčítání")
print("3 - násobení")
print("4 - dělení")
operace = int(input(""))

if (operace == 1):
    vysledek = a + b
elif (operace == 2):
    vysledek = a - b 
elif (operace == 3):
    vysledek = a * b
elif (operace == 4):
    vysledek = a / b   
if operace > 0 and operace < 5:
    print("Výsledek: %f" % (vysledek))
else:    
    print("Cybná volba")
print("Děkuji za použití kalkulajdy!")