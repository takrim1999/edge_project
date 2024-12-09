number = int(input("Your Number: "))
odd_list = []

for i in range(number):
    if i%2!=0:
        odd_list.append(i**2)

i=0
even_list = []
while i<number:
    if i%2==0:
        even_list.append(i/2)
    i+=1

print("Odd Numbers squared", odd_list)
print("Even Numbers divided by 2", even_list)