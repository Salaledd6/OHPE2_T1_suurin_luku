def suurin_luku(a, b, c, d, e):
   return max(a, b, c, d, e)


maara = int(input("Kuinka monta lukua haluat syöttää? "))
  #Kysytään käyttäjältä viisi lukua
luvut = []
for i in range(maara):
    luku = int(input(f"Anna luku {i+1}: "))
    luvut.append(luku)

 #Käytetään suurin_luku-funktiota suurimman luvun löytämiseksi
suurin = suurin_luku(*luvut)
print(f"Suurin luku on: {suurin}")






#def suurin_luku(luku1, luku2, luku3, luku4, luku5):
  #  suurin = max(luku1, luku2, luku3, luku4, luku5)
 #   return suurin

#l1 = int(input("Luku 1 > "))
#l2 = int(input("Luku 2 > "))
#l3 = int(input("Luku 3 > "))
#l4 = int(input("Luku 4 > "))
#l5 = int(input("Luku 5 > "))

#suurin = suurin_luku(l1, l2, l3, l4, l5)
#print("Suurin luvuista on: ", suurin)









#def suurin_luku(lista:list):
  #  suurin = max(lista)
 #   return suurin


#luvut = []


#for i in range(1,6):
 #   luvut.append(int(input(f"Luku {i} > ")))


#suurin = suurin_luku(luvut)
#print("Suurin luku on ", suurin)








 # def suurin_luku(lista:list):
   # suurin = lista[0]

   # for luku in lista[1:]:
     #   if luku > suurin:
      #      suurin = luku

    # return suurin


# luvut = []


# for i in range(1,6):
  #  luvut.append(int(input(f"Luku {i} > ")))


# suurin = suurin_luku(luvut)
# print("Suurin luku on ", suurin)