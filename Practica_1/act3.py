Cadena = "Parangaricutirimicuaro"
abc=[]
i=0
total = len(Cadena)

while i<total:
    letra = Cadena[i]
    if letra in abc:
        pass
    else:
        abc.append(letra)
    i+=1

# print(abc)

total2= len(abc)
# print(total2)
o=0
while o<total2:
    x=abc[o]
    total3= Cadena.count(x)
    print(x,":",total3)
    o+=1
