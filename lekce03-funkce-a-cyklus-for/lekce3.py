#print(1,2,3, sep="-", end="!!!")


#vek = int(input("kolik ti je"))
#print(vek + 1)


#jmeno = input("jmeno")
#print("tve jemeno je", len(jmeno), "dlouhe")

#print(abs(-7))

#print(round(3.14159, 10))


#print(min(range(2,10)) #zacina s 2 ale konci 9. 10 nepocita 

#print(max(2,3,-2) < 4)

# for i in range(2,10):  # range - funke pro cisla 
#     print(i)


# #loop:
# print("zacatek")
# for i in range(8,10):
#     print("cislo")
#     if(i % 2 == 0):
#         print("sude", i)
#     else:
#         print("Liche", i)
#     print("koned cyklu", i)
# print("hotovo")

# soucet = 0
# for i in range (0, 5):
#     print("i", i)
#     print("soucet na zacatku:", soucet)
#     soucet = soucet + i 
#     print("soucet na konci cyklu:", soucet)

# print("po cyklu:", soucet)

# for i in range (1,13):
#     print("mesic", mesic)
#     for tyden in range(1,6):
#         print("mesic:", mesic, "tyden:", tyden)
#         for den in range(1,8):
#             print("Mesic", mesic, "tyden", tyden, )
#     print("konec mesice", mesic)
# print("konec kalendare")

# jmeno = input("Jmeno?")
# for pismeno in jmeno:
#     print(pismeno, "!")


# while loop

# heslo = input("Zadej heslo")
# while heslo != "pyladies": 
#     print("Neprihlasena")
#     heslo = input("Zadej heslo")
# print("prihlasena")


# from random import randrange

# hod = randrange(1,7)
# while hod != 6:
#     print("Pado:", hod, "hazime znovu")
#     hod = randrange(1,7)
# print("vyhral si")


# from random import randrange

# hod = randrange(1,7)
# while hod > 1 and hod < 6:
#     if hod == 1:
#         print("Padlo:", hod, "Koncime")
#         break
#     print("Padlo:", hod, "hazime znovu")
#     hod = randrange(1,7)
# if hod == 1:
#     print("prohrala si")
# else:
#     print("Padlo:", hod, "vyhrala si")

# soucet = 0
# while True: # nebo while soucet < 10000:
#     odpoved = input("Zadej cislo (nebo 'konec')")
#     if odpoved == 'konec':
#         break

#     cislo = int(odpoved).  #nebo desetinne cisla float
#     if cislo < 0:
#         print("Zaporna cisla ignorujeme")
#         continue
#     soucte = soucet + cislo
#     print("Zatim mame:", soucet)
# print("Soucet", soucet)