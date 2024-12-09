start = int(input("Start Interval: "))
end = int(input("End Interval: "))
prime_list = []
def is_even(n):
    return not bool(n&1)

def is_prime(n):
    PrimeFlag = True
    if n in [0,1]:
        return False
    for i in range(2,int(n**.5)+1):
        if is_even(n):
            if n==2:
                return True
            return False
        else:
            if n%i==0:
                PrimeFlag=False
    return PrimeFlag

for j in range(start,end):
    if is_prime(j):
        prime_list.append(j)

print(prime_list)