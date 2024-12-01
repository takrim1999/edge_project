def is_prime(number):
    return not bool([i for i in range(2,int(number**0.5)+1) if number%i==0])
    # return [i for i in range(2,int(number**0.5)+1) if number%i==0]
        
print(is_prime(100001))