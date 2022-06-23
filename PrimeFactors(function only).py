import math

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
        for counter in range(z-1):
            PrimeFactor.pop(0)
    print('The prime factors of ' + str(num) + ' are' + factor_str[2:])

