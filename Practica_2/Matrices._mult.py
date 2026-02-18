x=[[5,6,13],[3,10,1],[2,11,3]]
y=[[1,2,17],[6,5,15],[3,11,12]]

z=[[0,0,0],[0,0,0],[0,0,0]]

res=0

for fila1 in range(len(x)):
    # print(x[fila1])
    print()
    for col2 in range(len(y[fila1])):
        for fila2 in range(len(y)):
            # print(y[fila2][col2])
            # print(x[fila1][fila2], y[fila2][col2])
            res += (x[fila1][fila2] * y[fila2][col2])
            
        
        # print()
        print(res)
        z[fila1][col2] = res
        res=0
        
# print(z)



