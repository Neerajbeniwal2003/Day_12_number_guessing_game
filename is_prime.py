def is_prime(num):
    if num==1:
        return False
    elif num==2:
        return True
    for i in range(1,num):
        if num%i==0:
            return False
    return True
print(is_prime(6))