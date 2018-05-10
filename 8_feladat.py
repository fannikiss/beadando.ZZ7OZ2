#62-es számrendszerig tudunk átváltani
base='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def v2r(n, b): #átalaktíja a megadott számot, a megadott számrendszerbe
    digits = ''
    while n > 0:
        digits = base[n % b] + digits
        n  = n // b
    return digits

def r2v(digits, b): #számrendszerből vált vissza
    n = 0
    for d in digits:
        n = b * n + base[:b].index(d)
    return n

def b2b(digits, b1, b2): #egy adott számrendszerből, egy adott számrendszerbe
    return v2r(r2v(digits, b1), b2)

print(v2r(124,62))
print(r2v('20',62))
