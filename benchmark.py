import time
import tracemalloc
from shor import shor_classical_simulation
from utils import generate_semiprime

def benchmark_shor(min_bits=4, max_bits=12, trials_per_bit=5):
    results = []
    for bits in range(min_bits, max_bits + 1):
        for _ in range(trials_per_bit):
            N = generate_semiprime(bits)
            tracemalloc.start()
            start_time = time.time()

            factors, period = shor_classical_simulation(N)

            elapsed = time.time() - start_time
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            success = factors is not None

            results.append({
                'bits': bits,
                'N': N,
                'factors': factors,
                'period': period,
                'time': elapsed,
                'memory': peak / 1024,  # in KB
                'success': success
            })

    return results
