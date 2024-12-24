import statistics
carSellingData = [
    {'Name' : "Company 1", 'sells' : [25,20,30,40,70,20,30]},
    {'Name' : "Company 2", 'sells' : [50,40,20,40,56,90,12]},
    {'Name' : "Company 3", 'sells' : [25,70,25,30,20,12,64]},
    {'Name' : "Company 3", 'sells' : [27,29,32,30,22,8,45]},
    {'Name' : "Company 4", 'sells' : [23,90,50,32,12,44,32]},
    {'Name' : "Company 5", 'sells' : [22,22,34,96,2,11,80]},
]

def analyzeData(payload):
    data_dict = {}
    for i in payload:
        # sum(i['sells'])/len(i)
        data_dict[i['Name']] = statistics.stdev(i['sells'])
    print(data_dict)
    for j in data_dict:
        if data_dict[j] == min(data_dict.values()):
            print(f"{j} is selling the lowest and Sell Standerd Deviation amount: {data_dict[j]}")

analyzeData(carSellingData)