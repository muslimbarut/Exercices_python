#```print("Amakuru yawe?\n")
#print("A","B","c\n", sep="   -     ")
#print("2026", "01", "03\n", sep="        ")
#print("Mwiriwe",end="          ")
#print("Neza\n")
#izina = "Kamari"
#amafra = 1000.7654
#print(f"amakuruyawe {izina} ufise amafara \nnga {amafra: .3f}")
#print(type("+32"))  
#imyaka = 18
#izina = 'Muslim ni'
#print("Imyaka ya ",izina,imyaka)
#name = input("izina ryawe: ")
#if (name == "Muslim"):
    #print(f"Hello, {name}")
#elif (name == "Peter"):
    #print(f"Hello, {name}")
#elif (name == "Arthur"):
   # print(f"Hello, {name}")
#else:
    #print(f"Wewe urinde?")
    
#gukora system
#email = input("Shiramwo email: ")
#password = input("shiramwo password: ")
#if (email == "muslim@gmail.com"):
    #Yego
    #print("Vyagenze neza!")
    #if (int(password) == 1234567):
        #print(f"login nziza ya {email}!")
    #else:
        #print("password siyo")        
#else:
   # print("Niwiyandikishe, email yawe \nntayirimwo?")
   
   
   
#email = input("Shiramwo email: ")
#password = input("shiramwo password: ")
#if (email == "muslim@gmail.com" or int(password) == 12345):
    #print("washizemwo neza email hamwe na password!")
#else:
    #print("ivyo washizemwo sivyo?")
    
#izina = input("witwande: ")
#match izina:
    #case "muslim":
 #       print(f"Hello, {izina}")
 #   case "Barut":
       # print(f"Bite, {izina}") 
   # case "Salf":      
     #   print(f"amakuru, {izina}")
  #  case _:
       # print("wihenze subiramwo")
       
#fo = input("andika ijambo ryose ushaka \nriza kwiyafisha incuro 10 andika: ")
#for c in range(11,-30,-2):
  #  print(c)
  
#print(range(60))

#umuba1 = int(input("Shiramwo igiharuro: "))
#umuba2 = int(input("Shiramwo ikindi giharuro: "))
#for igi in range(umuba1,umuba2):
    #if igi % 1 == 0:
    #    print(f"{igi}. Even number")
 #   else:
      #  print(f"{igi}. Odd number")
    
#num = 1
#while num > 10:
#    print(num)
  #  num += 1
#else:
 #   print("Good!")
#for v in range(0, 51):
    #if v % 2 == 0:
 #       print(f"{v}. Even")
#    else:
       # print(f"{v}. Odd")
#for d in range(1,31):
 #   if d == 10 or d == 20:
    #    continue
  #  print(d)
     
sandu = ["Umunyu","Umuceri","Ubugari","Amakoto"]
#print(sandu)  
sandu.append("ibiharage")
#print(sandu)
#sandu.remove("Umunyu")
#print(sandu)
#guha = len(sandu)
#print(sandu)
#print(f"bingana uku: {guha}")
#print(sandu[4])

#for t , b in enumerate(sandu):
    #print(f"{t}. {b}")
    
    
#Dictionary

ibicu = {
    "Umuceri": 15000,
    "Amakoto": 8000,
    "ibiharage": 3000,
    "umunyu": 1500,
}
#print(ibicu)
ibicu["Igitoke"] = 5000
#print(ibicu)
ibicu.pop("Amakoto")
#print(ibicu)
#ivyo = len(ibicu)
#print(f"Ibicuruzwa: {ivyo}")
#suzuma = "Igitoke" in ibicu
#print(f"arimwo: {suzuma}")
for igici, ikida in ibicu.items():
    print(igici,": ", str(ikida)+"Fbu")