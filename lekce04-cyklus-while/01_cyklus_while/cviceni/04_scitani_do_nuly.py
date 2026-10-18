# Cvičení 4 – Cyklus while
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel postupně zadává čísla. Sčítej je. Jakmile zadá 0,
#    přestaň se ptát a vypiš celkový součet.


cislo = 1
soucet = 0
while cislo != 0:
    cislo = int(input("Zadej číslo (0 = konec): "))
    if cislo < 0:
        continue
    soucet = soucet + cislo
print ("celkovy soucet", soucet)    


