
def isPrime(num):
    if num < 2:
        return False

    # keresse az osztókat a szám gyökéig

    for i in range(2, int(math.sqrt(num)) + 1):

        if num % i == 0:
            return False

    return True

