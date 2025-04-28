import math
import random

"The functions required to run a classical exmaple of shor's algorithm, cut from this repo's original shors.py"

def find_period(a, N):
    """Brute-force period finding."""
    r = 1
    while pow(a, r, N) != 1 and r < N:
        r += 1
    if r == N:
        return None
    return r

def shor_classical_simulation(N, max_attempts=5, verbose=False):
    """Simulate Shor's algorithm classically for integer N."""
    if verbose:
        print(f"\nAttempting to factor N = {N}")

    for attempt in range(1, max_attempts + 1):
        a = random.randint(2, N - 2)
        g = math.gcd(a, N)
        if verbose:
            print(f"\n[Attempt {attempt}] Chose a = {a}")
            print(f"  gcd({a}, {N}) = {g}")

        if g != 1:
            if verbose:
                print(f"Found factor by luck: ({g}, {N // g})")
            return (g, N // g), 0

        r = find_period(a, N)
        if r is None or r % 2 != 0:
            if verbose:
                print(f"Invalid period r = {r}, trying new a.")
            continue

        ar2 = pow(a, r // 2, N)
        if verbose:
            print(f"  Period r = {r}")
            print(f"  a^(r/2) = {a}^{r//2} mod {N} = {ar2}")

        if ar2 == N - 1 or ar2 == 1:
            if verbose:
                print(f" a^(r/2) ≡ ±1 mod N, trying new a.")
            continue

        factor1 = math.gcd(ar2 - 1, N)
        factor2 = math.gcd(ar2 + 1, N)

        if verbose:
            print(f"    gcd({ar2}-1, {N}) = {factor1}")
            print(f"    gcd({ar2}+1, {N}) = {factor2}")

        if factor1 * factor2 == N and factor1 not in (1, N) and factor2 not in (1, N):
            if verbose:
                print(f"\nSuccess! Factors of {N} are {factor1} and {factor2}")
            return (factor1, factor2), r

        if verbose:
            print(f"Found trivial or incorrect factors, trying new a.")

    if verbose:
        print("\nFailed to find factors after multiple attempts.")
    return None, None