

suorakulmio1_str = input('Mikä on suorakulmion kanta?: ')
suorakulmio2_str = input('Mikä on suorakulmion korkeus?: ')
kanta = int(suorakulmio1_str)
korkeus = int(suorakulmio2_str)

print('suorakulmion pinta-ala on : ' + str(kanta*korkeus))
print('Suorakulmion piiri on: ' + str((korkeus*2)+(kanta*2)))


