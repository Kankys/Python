# Relační operátory
#Podívejme se na seznam relačních operátorů, které se ve výrazech podmínek používají:

#Význam	Operátor
#Rovnost	==
#Je ostře větší	>
#Je ostře menší	<
#Je větší nebo rovno	>=
#Je menší nebo rovno	<=
#Nerovnost	!=
#Obecná negace	not
#Častou chybou začátečníků ve psaní výrazů bývá záměna za jedno rovnítko =. Je třeba si uvědomit že = slouží k přiřazování hodnot do proměnných.

#== slouží k testování hodnot proměnných

#Používáme operátor == pro zjištění rovnosti dvou hodnot nebo hodnot proměnných.
# Pokud chceme výraz znegovat, napíšeme před něj klíčové slovo not. 
# Blok podmínky se skládá z tabulátorového odsazení! 
# Každý příkaz se tedy píše pod výraz podmínky na samostatný řádek, odsazený tabulátorem:

 
a = int(input("Zadej nějaké číslo, ze kterého spočítám odmocninu: "))
if (a > 0):
     print("Zadal jsi číslo větší než 0, to znamená, že ho mohu odmocnit!")
     odmocnina = a ** (1 / 2)
     print("Odmocnina z čísla %d je %f" % (a, odmocnina))
print("Děkuji za zadání")    

# A verze co nás bude varovat při zadání 0 nebo menším k odmocnění

a = int(input("Zadej nějaké číslo, ze kterého spočítám odmocninu: "))
if (a > 0):
    print("Zadal jsi číslo větší než 0, to znamená že ho mohu odmocnit!")
    odmocnina = a ** (1 / 2)
    print("Odmocnina z čísla %d je %f " % (a, odmocnina))
if (a <= 0):
    print("Odmocnina ze záporného čísla neexistuje!")    
print("Děkuji za zadání")

# Použí else:

a = int(input("Zadej nějaké číslo, ze kterého spočítám odmocninu: "))
if (a > 0):
    print("Zadal jsi číslo větší než 0, to znamená, že ho je možné odmocnit!")
    odmocnina = a ** (1 / 2)
    print("Odmocnina z čísla %d je %f " % (a, odmocnina))
else:
    print("Odmocnina ze záporného čísla neextistuje!")    
print("Děkuji za zadání") 

# Další využití else:

a = 0 #  deklarace proměnné s hodnotou 0
if (a == 0): # pokud je hodnota proměnné 0, změňíme hodnotu na 1
    a = 1
else: # pokud je hodnota proměnné 1, změňíme hodnotu na 0
    a = 0
print(a)