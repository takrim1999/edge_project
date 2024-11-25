pw = int(input ("Enter the weight: "))
if pw>0.1 and pw<=5: 
    print('shipping cost is 5$')
elif pw>5 and pw <=10: 
    print('Shipping cost is 10$') 
elif pw>10 and pw <=15: 
    print('Shipping cost is 15$') 
elif pw>15 and pw <20: 
    print('Shipping cost in 20$')
elif pw>20:
    print("Not Supported!")