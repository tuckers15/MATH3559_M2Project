from benchmark import benchmark_shor
from plotter import plot_runtime, plot_memory, plot_success_rate
from shor import shor_classical_simulation

def main():
    results = benchmark_shor(min_bits=4, max_bits=30, trials_per_bit=3)

    plot_runtime(results)
    plot_memory(results)
    plot_success_rate(results)

    
    print("\nRunning a verbose demo on N = 55 as an example")
    shor_classical_simulation(55, verbose=True)

if __name__ == "__main__":
    main()
