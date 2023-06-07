import math
from sys import exit as ex

def PrimeFactors(num):
    def Quotient():
        quotient = 1
        for n in PrimeFactor:
            quotient *= n
        return quotient
    number = abs(num)
    x = num
    global PrimeFactors
    PrimeFactor = [ ]
    composites = set(j for i in range(2, math.ceil(math.sqrt(number))) for j in range(i*2, number, i))
    primes = [x for x in range(2, number) if x not in composites]
    for prime in primes:
        while x % prime == 0:
            PrimeFactor.append(prime)
            x /= prime
    if num != number:
        PrimeFactor.append(-1)
    if PrimeFactor.sort() != None:
        PrimeFactor = PrimeFactor.sort()
    factor_str = ''
    for y in PrimeFactor:
        z = PrimeFactor.count(y)
        if z == 1:
            factor_str += (f' * {y}')
        else:
            factor_str += (f' * {y}^{z}')
        for _ in range(z-1):
            PrimeFactor.pop(0)
    return factor_str[2:]

try:
    num = int(input("Enter the number you wish to find the prime factor of: "))
except ValueError:
    ex("Incorrect value entered. Please try again.")
print(f"Prime factorisation of {num}: {PrimeFactors(num)}")
