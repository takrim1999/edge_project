def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

def MyFunction():
    original_list = []
    count = int(input("How many numbers do you want to input: "))
    for i in range(count):
        original_list.append(int(input("Your Integer Number: ")))
    print("Original List: ", original_list)
    print("Squared List: ", [i**2 for i in original_list])
    print("Factorial List: ", [factorial(i) for i in original_list])
MyFunction()