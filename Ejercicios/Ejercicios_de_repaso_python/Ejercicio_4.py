
#Bubble Sort 
def sort(array):
    for i in range(len(array),1,-1):
        for j in range(0,i-1):
            if array[j]<array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]

lista = [1,6,3,4,5]
sort(lista) # muta el array original

print(lista)
