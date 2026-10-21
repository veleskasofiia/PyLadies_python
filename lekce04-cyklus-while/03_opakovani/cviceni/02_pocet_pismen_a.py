# Cvičení 2 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá slovo. Spočítej, kolikrát se v něm objeví
#    písmeno "a", a výsledek vypiš.


pocet = 0
slovo = input("zadej slovo:")
for pismeno in slovo:
    if pismeno == "a":
        pocet = pocet + 1
print("pismeno 'a' je ve slove", pocet, "krat")
