givenList = [5,'xy',11,'abcd',33,110.50]
returnList = [len(i) for i in givenList if type(i)==str]
print(returnList)