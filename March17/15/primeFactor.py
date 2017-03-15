#Project Euler problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#solution options: Fermat factorisation, Quadratic sieve, Pollard's Rho algorithm

def PrimeFactor(n):
    m = n
    while n%2==0:
        n = n//2
    if n == 1:         # check if only 2 is largest Prime Factor 
        return 2
    i = 3
    sqrt = int(m**(0.5))  # loop till square root of number
    last = 0              # to store last prime Factor i.e. Largest Prime Factor
    while i <= sqrt :
        while n%i == 0:
            n = n//i       # reduce the number by dividing it by it's Prime Factor
            last = i
        i+=2
    if n> last:            # the remaining number(n) is also Factor of number 
        return n
    else:
        return last
print(PrimeFactor(600851475143)) 