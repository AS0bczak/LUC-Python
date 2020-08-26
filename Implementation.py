from multiprocessing import Pool
import time



def generating_special_sequence(n):
    k = list()
    k.insert(0, 2)
    m = 0

    while n != 1:
        m = m + 1
        if n % 2 == 1:
            n = n - 1
            k.insert(m, 1)
        else:
            n = n / 2
            k.insert(m, 0)
    return k, m


def compute_v2n(vn, n):
    return (vn*vn - 2) % n


def compute_v2n1(vn, vn1, P, n):
    return (P * vn*vn - vn*vn1 - P) % n


def compute_v2n11(vn, vn1, P, n):
    return (vn*vn1 - P) % n


if __name__ == "__main__":
    start = time.time()
    for i in range(100):
        p = 11
        q = 3
        n = p * q
        e = 7
        P = 5
        k, m = generating_special_sequence(n)
        vn = P
        vj = 2
        while m != 0:
            if k[m] == 1:
                with Pool(processes=2) as pool:
                    p1 = pool.apply_async(compute_v2n1, args=(vn, vj, P, n,))
                    p2 = pool.apply_async(compute_v2n, args=(vn, n,))
                    vn = p1.get()
                    vj = p2.get()
            elif k[m] == 0:
                with Pool(processes=2) as pool:
                    p1 = pool.apply_async(compute_v2n, args=(vn, n,))
                    p2 = pool.apply_async(compute_v2n11, args=(vn, vj, P, n,))
                    vn = p1.get()
                    vj = p2.get()

            else:
                pass
            m = m - 1
    end = time.time()
    print(end - start)
    print("Czas ", )


