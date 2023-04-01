import random

array = []
size = 10

for i in range(size):
    array.append(random.randint(1,100))

def qsort(array,first,last):
    if first >= last:
        return
        
    f = first
    l = last
    mid = array[int( (f+l)/2 )]

        
    while f <= l:
            while array[f] < mid:
                f += 1
            while array[l] > mid:
                l -= 1
            if f <= l :
                count = array[f]
                array[f] = array[l]
                array[l] = count
                f += 1
                l -= 1
    
    qsort(array,first,l)   
    qsort(array,f,last)

qsort(array,0,size-1)
print(f'Normal list : {array}')

array.reverse()
print(f'Reversed list : {array}')