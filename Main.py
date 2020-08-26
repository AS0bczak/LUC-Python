import time


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('odwrotność modularna nie istnieje')
    else:
        return x % m


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)


def calculateLegendre(a, p):
    if a >= p or a < 0:
        return calculateLegendre(a % p, p)
    elif a == 0 or a == 1:
        return a
    elif a == 2:
        if p % 8 == 1 or p % 8 == 7:
            return 1
        else:
            return -1
    elif a == p - 1:
        if p % 4 == 1:
            return 1
        else:
            return -1
    elif not isPrime(a):
        factors = factorize(a)
        product = 1
        for pi in factors:
            product *= calculateLegendre(pi, p)
        return product
    else:
        if ((p - 1) / 2) % 2 == 0 or ((a - 1) / 2) % 2 == 0:
            return calculateLegendre(p, a)
        else:
            return (-1) * calculateLegendre(p, a)


def encrypt(n, P, N):
    licznik = 1
    now = P
    prev =2
    while licznik != n:
        new = P * now - prev
        new = new % N
        prev = now
        now = new
        licznik = licznik + 1
    return now


def coprime2(x, y):
    return gcd(x, y) == 1


def gen(p, q, M):
    D = pow(M, 2) - 4
    return p*q, D, lcm(p - calculateLegendre(D, p), q - calculateLegendre(D, q))


M = 5
#print("Wiadomość ", M)
p = 11
q = 3
e = 1103
N, D, S = gen(p, q, M)


if coprime2(e, (p-1)*(q-1)*(p+1)*(q+1)) == False:
    print("inna wartość e")
    exit(0)

if coprime2(N, M) == False:
    print("Error")

start = time.time()
for i in range(1000000):
    Mprim = encrypt(e, M, N)

end = time.time()
print(end - start)
print("Wiadomość zaszyfrowana ", Mprim)
d = modinv(e, int(S))
print("d ", d)
Mbis = encrypt(d, Mprim, N)
print("Wiadomość po deszyfracji ", Mbis)
if Mbis == M:
    print("Wiadomość została poprawnie zdeszyfrowana")
else:
    print("Wiadomość została błędnie zdeszyfrowana")