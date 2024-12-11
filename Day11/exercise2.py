from array import array as arr

myArray = arr('i',[10,5,15,4,6,20,9])
evenArray = arr('i',[])
print(myArray)
for i in myArray:
    if i%2==0:
        evenArray.append(i)
print(evenArray)