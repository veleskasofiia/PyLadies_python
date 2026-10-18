# Cvičení 3 – Cyklus while
# Doplň kód pod zadání a soubor spusť (Run).

# Ptej se uživatele "Jaké je hlavní město Česka? " tak dlouho,
#    dokud nenapíše "Praha". Pak vypiš "Správně!".


zadej_mesto = input("Jaké je hlavní město Česka?")
while zadej_mesto != "Praha":
    print("spatne heslo")
    zadej_mesto = input("Jaké je hlavní město Česka?")
    print("ano")