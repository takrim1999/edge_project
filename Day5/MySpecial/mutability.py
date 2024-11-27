try:
    myList = [1,2,3,4,5]
    myList[3] = 75
    myTuples = (1,2,3,4,5)
    myTuples[3] = 75
except TypeError:
    print(TypeError)