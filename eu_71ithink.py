# def gcd(a:int,b:int):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)
    
# lim=10000
# total =0

# for n in range(1,lim):
#     l2 = [1]*(lim-n)
#     for i in range(1,len(l2)+1):
#         if gcd(i+n,n)>1:
#             l2[i-1]=0
#     # print(l2)
#     l3 = [f'{n}/{i+1+n}' for i in range(len(l2)) if l2[i]]
#     # print(len(l3),l3)
#     total+=len(l3)
# print(total)

####

# import math

# lim = 8
# total = 0

# for n in range(1, lim):
#     count = 0
#     for i in range(1, lim - n):
#         if math.gcd(i + n, n) == 1:
#             count += 1
#     total += count

# print(total)

####

import contextlib
import math
from itertools import islice

def iter_index(iterable, value, start=0, stop=None):
    "Return indices where a value occurs in a sequence or iterable."
    # iter_index('AABCADEAF', 'A') → 0 1 4 7
    seq_index = getattr(iterable, 'index', None)
    if seq_index is None:
        iterator = islice(iterable, start, stop)
        for i, element in enumerate(iterator, start):
            if element is value or element == value:
                yield i
    else:
        stop = len(iterable) if stop is None else stop
        i = start
        with contextlib.suppress(ValueError):
            while True:
                yield (i := seq_index(value, i, stop))
                i += 1

def sieve(n):
    "Primes less than n."
    # sieve(30) → 2 3 5 7 11 13 17 19 23 29
    if n > 2:
        yield 2
    data = bytearray((0, 1)) * (n // 2)
    for p in iter_index(data, 1, start=3, stop=math.isqrt(n) + 1):
        data[p*p : n : p+p] = bytes(len(range(p*p, n, p+p)))
    yield from iter_index(data, 1, start=3)


def factor(n):
    "Prime factors of n."
    # factor(99) → 3 3 11
    # factor(1_000_000_000_000_007) → 47 59 360620266859
    # factor(1_000_000_000_000_403) → 1000000000000403
    for prime in sieve(math.isqrt(n) + 1):
        while not n % prime:
            yield prime
            n //= prime
            if n == 1:
                return
    if n > 1:
        yield n

def totient(n):
    "Count of natural numbers up to n that are coprime to n."
    # https://mathworld.wolfram.com/TotientFunction.html
    # totient(12) → 4 because len([1, 5, 7, 11]) == 4
    for prime in set(factor(n)):
        n -= n // prime
    return n

lim = 1000000
# phi = totient(lim)

# total = 0
# for n in range(1, lim):
#     total += phi

print(lim)
print(sum([totient(i) for i in range(2,lim+1)]))

