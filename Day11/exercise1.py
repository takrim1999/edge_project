from array import array as createArray
array = [10,20,30,40,50]
array = createArray('i', array)
array.insert(1,60)
for i in array:
    print(i)
array.remove(50)
print(array)