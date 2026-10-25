

# vek_uzivatele = 1
# print(vek_uzivatele) #pokud jsou zavorky - je funkce



#o!!!dsud zacina definice toho co chceme zavolat

# max_hodnota = 10

# def vypis_cislo_do_max_hodnoty(jmeno_volani, max_hodnota, ukaz_caru = True):           #jenom jsme definovali funkce, ale ted nic nestane
#     for aktualni_cislo in range(1, max_hodnota):
#         print(jmeno_volani + ":" +str(aktualni_cislo))
#     if ukaz_caru:
#         print("-"*30) 

# #!!!!odsud zacna volani
    
# vypis_cislo_do_max_hodnoty("Volani A", 10)
# vypis_cislo_do_max_hodnoty("Volani B", 100)
# vypis_cislo_do_max_hodnoty( "Volani C", 1000, False)

# # vek = 7


# cislo_od_uzivatele = input("Zadej cislo:")

def cena_mhd(vek):
    print("pocitam cenu listku pro vek", vek)

    if vek < 6:
        # print("cena 0")
        return 0
    elif vek < 18:
        # print("cena 39")
        return 39
    elif vek < 65:
        # print("cena 50")
        return 50
    else: 
        # print("cena 0!")
        return 0

zustatek_uctu = 100
cena_jizdenky = cena_mhd(7)
print("vysledna cena je", cena_jizdenky)
cena_jizdenky = cena_jizdenky/1.5
print("sleva", cena_jizdenky)

zustatek_uctu = zustatek_uctu - cena_jizdenky