carSellingData = [
    {'Name' : "Company 1", 'sells' : 20},
    {'Name' : "Company 2", 'sells' : 30},
    {'Name' : "Company 3", 'sells' : 15},
    {'Name' : "Company 4", 'sells' : 50},
    {'Name' : "Company 5", 'sells' : 70},
]

total_sels = []
for i in carSellingData:
    total_sels.append(i['sells'])
average = int(sum(total_sels)/len(total_sels))
print("Average Sells: ", average)
for j in carSellingData:
    if average<j['sells']:
        print("Name: ", j['Name'])
        print("Total Sells : ", j['sells'])