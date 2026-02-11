x = [1,2,4,4,4,5,7,9,11,11,13,14,15,16,16]
nuevo = []
# y = set(x)
# print(y)

total = len(x)
print(total)
i=0
while i<total:
    num = x[i]
    if num in nuevo:
        pass
    else:
        nuevo.append(num)
    i+=1

print(nuevo)