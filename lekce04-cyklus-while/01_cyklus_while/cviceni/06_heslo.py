# Cvičení 6 – Cyklus while
# Doplň kód pod zadání a soubor spusť (Run).

# Ptej se na heslo. Když uživatel zadá "pyladies", vypiš "Vítej!"
#    a skonči. Když se splete třikrát, vypiš "Zablokováno." a skonči taky.
#    Z cyklu se v obou případech dostaneš příkazem break.

tries = 0
while True:
    heslo = input("Zadej heslo:")
    tries = tries + 1
    if heslo == "pyladies":
        print("Vitej!")
        break
    zbyva = 3 - tries
    if zbyva == 0:
        print("zablokovano")
        break



# for range in (3):
#     heslo = int(input("Zadej heslo:"))
#     if heslo == "pyladies":
#         print("Vitej")
#         break
#     print("zkis jeste")
# else:
#     print("Zablokovano")
    




#heslo = input("Zadej heslo")
# while heslo != "pyladies": 
#     print("Neprihlasena")
#     heslo = input("Zadej heslo")
# print("prihlasena")
