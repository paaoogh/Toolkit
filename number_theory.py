def reduce_mod(a, mod):
    a %= mod
    if a<0:
        a+=mod
    return a

def gcd(a,b):
    #greatest common divider
    while b!=0:
        r = a%b
        a = b
        b = r
    return a

def lcm(a,b):
    #locest common multiplier
    return a*b/(gcd(a,b))


def gcd_ex(a,b):
    #linear combination of gcd: ax + by = d
    if b==0:
        return a,1,0
    sa = 1
    sb = 0
    ta = 0
    tb = 1

    while b!=0:
        rem = a%b
        quo = a/b
        a = b
        b = rem

        sc = sa - quo*tb
        sa = sb
        sb = sc

        tc = ta- quo*tb
        ta = tb
        tb = tc 
    return a,sa,ta


def mod_inverse(a,n):
    #missing
    return

def ReadNBaseB(b, digits):
    #digits[i] = coefficient of b**i
    suma = 0
    power = 1

    for d in digits:
        suma += power*d
        power *= b
    return suma 

def WriteNBaseB(n,b):
    #wrtie a number in base b
    #does not reverse the digits!!
    digits = []

    while n:
        digits.append(n%b)
        n /= b 
    return digits


