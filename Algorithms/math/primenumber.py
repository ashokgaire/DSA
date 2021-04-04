'''
generate prime number using Sieve Eratosthenes algorithm 

'''


def getPrime(n):

    if (n == 1):
        return None

    prime = [None]*(n+2)
    primesquare = [None]*(n*n*2)
    
    #for stroring primes upto n 
    a = [0]*n

    #create a boolean array "prime[0..n]"
    # and initialize all entries it as true
    # a value in prime[i] will finally be false
    #if i is not a prime, else True

    for i in range(2,n+1):
        prime[i] = True


    #create a boolean array "primesquare[0..n*n+1]"
    # and initialize all entries it as false
    # a value in prime[i] will finally be true
    #if i is squareof  prime, else false

    for i in range((n * n +1)+1):
        primesquare[i] = False

    # 1 is not a prime number
    prime[1] = False

    p = 2

    while(p * p <=n):
        # if prime[p] is not changed,
        # then it is a prime

        if (prime[p] == True):
            # update all multiples of p
            i = p * 2
            while(i<=n):
                prime[i] = False
                i += p 
        p += 1

    j = 0
    for p in range(2,n+1):
        if(prime[p] == True):
            #Storing primes in an array
            a[j] = p

            # Update value in primeSquare[p*p]
            #if p is prime
            primesquare[p*p] = True
            j+=1
    #return a    (if you testing this code)
    return a,prime,primesquare



a,b,c = getPrime(10001)
print(a)
