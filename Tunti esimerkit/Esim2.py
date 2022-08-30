
#wihle esim 1
#niin kauan kui maksettu rahamäärä < annettu hinta
#anna kolikko

#hinta = int(input("Paljon maksaa?"))
#maksettu = 0
#while maksettu < hinta :
 #   maksettu = maksettu + 1
  #  print("maksetaan 1 euro lisää")
   # print(f"maksettavaa jäljellä {hinta - maksettu}")
#print("kahvit maksettu kokonaan")

#while esim 2 "ohjelma valikko"
#  command = command.lower()
# while not (command == "lopeta" or command == "Lopeta"):

#command = ""
#while command != "lopeta":
#    command = input("Anna komento")
#    if command == "tulosta":
#        print("tulostetaan")
#        print("jotain")
#    elif command == "lopeta":
#        print("kommentoi: tulosta, help, lopeta")
#    elif command == "lopeta":
#        print("ohjelma sammutetaan")
#        #break lopettaisi silmukan tähän testaamatta while ehtoa uudestaan
#    else:
#        print("en ymmärtänyt, anna toinen komento")
#    print("ohjelma käynnissä")
#print("ohjelma lopetettu")



#import random
#toistot = 0
#heitot_yhteensä = 0
#while toistot < 100000:

#    noppa1 = noppa2 = heitot = 0
#    while (noppa1!=6 or noppa2!=6):
#        noppa1 = random.randint(1,6)
#        noppa2 = random.randint(1,6)
#        heitot = heitot + 1
    #print(f"Tarvittiin {heitot:d} heittoa.")
#    toistot = toistot + 1
#    heitot_yhteensä = heitot_yhteensä + heitot

#heitot_keskimäärin = heitot_yhteensä/toistot
#print(f"Heitot keskimäärin: {heitot_keskimäärin:6.2f}")