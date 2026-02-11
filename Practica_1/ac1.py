Toneladas_Cereal=[12,21,16,15,20,18,6,10,12,14,15,12]
Lista_Mayor=[]
Lista_Menor=[]
suma=0
for i in Toneladas_Cereal:
    suma += i 

promedio = suma/len(Toneladas_Cereal)
print(promedio)

for i in Toneladas_Cereal:
    if(i>promedio): 
        # print(i)
        Lista_Mayor.append(i)
    else:
        Lista_Menor.append(i)
        


print(Lista_Mayor)


#Promedio de alumnos








