import math

def primes(n) -> list[int]:
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

def is_prime(m) -> bool:
    '''check if the given number is prime'''
    try:
        m = int(m)
    except:
        return False
    if m<0:
        return False
    n=m+1
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return (([2] + [2*i+1 for i in range(1,(n)//2) if sieve[i]])[-1] == m)

def factors(n) -> list:
    '''return a list of prime factors'''
    factors = []
    while n%2==0 and n!=0:
        factors.append(2)
        n//=2
    for i in range(3,int(math.sqrt(n)+1),2):
        while n%i==0:
            factors.append(i)
            n//=i
    if n>2:
        factors.append(n)
    return sorted(factors)