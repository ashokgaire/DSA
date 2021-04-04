''' program to find count divisor using Sieve Eratosthenes prime generation algoritm'''

import primenumber


def countDivisors(n):
    # if number is 1,then it will have only 1 as a factor
    if(n == 1):
        return 1

    # a for storing primes upto n 
    a,prime,primesquare = primenumber.getPrime(20)

    # total number of distinct divisor
    ans = 1

    #loop for counting factors of n
    i = 0
    while(1):
        # a[i] is not less than cube root n
        if(a[i] * a[i] * a[i] > n):
            break

        # calculating power of a[i] in n.
        cnt = 1 # cnt is power of prime a[i] in n 
        while (n % a[i] == 0): # if a[i] is a factor of n
            n = n / a[i]
            cnt = cnt + 1 # incrementing power

        #calculating number of divisors
        # if n =a^p * b^ q then total
        #divisor of n are (p+1)*(q+1)
        ans = ans * cnt
        i +=1


    # if a[i] is greate than cube root of n

    n = int(n)
    # first case
    if (prime[n] == True):
        ans = ans * 2

    # second case
    elif (primesquare[n] == True):
        ans = ans * 3

    # Third case
    elif (n !=1):
        ans = ans * 4

    return ans


### DRIVER code #######

print(countDivisors(28))

