# Program analyzuje délku zadaného jména. 
# Pokud je délka jména mezi třemi a deseti znaky, vypíše, že má uživatel normální jméno. 
# V ostatních případech vypíše, že je jméno příliš krátké nebo dlouhé.

jmeno = input("Zadej své jméno: ")
if len(jmeno) >= 3 and len(jmeno) <= 10:
 print("Jmeno máš normálně dlouhe")
else:
    print("Nemáš normální jméno!")