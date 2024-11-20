# reading from an array

array = [1,2,3,4,5]
print(array[1])

# Traversing an array

array = [1,2,3,4,5]
for i in array:
    print(i)
    
# delete from end of array

def RemoveLast(array,length):
    if length > 0:
        array[length-1] = 0

def RemoveAti(array,i,length):
    if(length > 0):
        for i in range(i+1,length):
            array[i-1] = array[i]
#INsert at the end

def InsertEnd(array,n,length,capacity):
    if length < capacity:
        array[length] = n

#Insert At i

def InsertAti(array,i,n,length):
    for i in range(length-1,i-1,-1):
        array[i+1] = array[i]
        
    array[i] = n
    


