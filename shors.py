import random
import math
import time
import matplotlib.pyplot as plt

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

# Benchmarking the simulation for increasing semiprimes
def benchmark_shor(min_bits=4, max_bits=12):
    results = []
    for bits in range(min_bits, max_bits + 1):
        # Generate small semiprime
        p = random.getrandbits(bits // 2)
        q = random.getrandbits(bits // 2)
        p, q = max(p, 3), max(q, 3)
        if p % 2 == 0: p += 1
        if q % 2 == 0: q += 1
        N = p * q

        start_time = time.time()
        factors, period = shor_classical_simulation(N)
        elapsed = time.time() - start_time

        results.append({
            'bits': bits,
            'N': N,
            'factors': factors,
            'period': period,
            'time': elapsed
        })

    return results

# Run the benchmark
benchmark_results = benchmark_shor()

# Plotting
bit_lengths = [r['bits'] for r in benchmark_results]
times = [r['time'] for r in benchmark_results]

plt.figure(figsize=(10, 6))
plt.plot(bit_lengths, times, marker='o')
plt.title("Classical Simulation of Shor's Algorithm")
plt.xlabel("Bit length of N")
plt.ylabel("Runtime (seconds)")
plt.grid(True)
plt.show()

# run verbose demo on a specific small N
shor_classical_simulation(55, verbose=True)
