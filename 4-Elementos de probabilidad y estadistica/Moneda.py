import random
lst=['Aguila','Sello']

aguila=0
sello=0

for i in range(15):
    tiro=random.choice(lst)
    if tiro == 'Aguila':
        aguila+=1
    else:
        sello+=1

if (aguila > sello):
    print('< Agila Gano >')
else:
    print('< Sello Gano >')

print("Suma Aguila: ", aguila)
print("Suma Sello: ", sello)
