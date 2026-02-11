Cadena = "Parangaricutirimicuaro"

a = list(set(Cadena))
a.sort()
print(a)

total2= len(a)
# print(total2)
o=0
while o<total2:
    x=a[o]
    total3= Cadena.count(x)
    print(x,":",total3)
    o+=1

