import random


"Get random semiprimes of given bit length"
def generate_semiprime(bits):
    p = random.getrandbits(bits // 2)
    q = random.getrandbits(bits // 2)
    p, q = max(p, 3), max(q, 3)
    if p % 2 == 0: p += 1
    if q % 2 == 0: q += 1
    return p * q
