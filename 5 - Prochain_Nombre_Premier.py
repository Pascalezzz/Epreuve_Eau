count = 1
#Fonction qui teste si nombre est premier
def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

#Fonction qui teste si le nombre suivant est premier
def is_n_plus_1_prime(num):
    if type(num) != int:
        print("-1")
        exit()

    global count
    if isprime(num+count):
        print(num+count)
        exit()
    else:
        count+=1
        is_n_plus_1_prime(num)

#Run code  
print(is_n_plus_1_prime(14))