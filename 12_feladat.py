
def isPrime(num):
    if num < 2:
        return False

    # keresse az osztókat a szám gyökéig

    for i in range(2, int(math.sqrt(num)) + 1):

        if num % i == 0:
            return False

    return True

def main():

    prime_srsz = int(input('Hanyadik prímet keressem: '))
    primes = []
    prime_num = 1
    prime_index = 1

    if prime_srsz<100000 :
        while prime_index < prime_srsz+1:
            prime_num += 1
            if isPrime(prime_num):
                primes.append(prime_num)
                prime_index += 1


        keresett_prim = primes[prime_index-2]
        print('A keresett prím:',str(keresett_prim))

    else:
        print('túl sok idő')


main()
