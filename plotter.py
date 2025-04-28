import matplotlib.pyplot as plt
import numpy as np

def plot_runtime(results):
    bit_lengths = [r['bits'] for r in results]
    times = [r['time'] for r in results]
    plt.figure(figsize=(10,6))
    plt.plot(bit_lengths, times, marker='o')
    plt.title("Runtime vs Bit Length")
    plt.xlabel("Bit length")
    plt.ylabel("Runtime (seconds)")
    plt.grid(True)
    plt.savefig("plots/runtime_plot.png")
    plt.close()

def plot_memory(results):
    """Plot average memory usage vs bit length."""
    bit_lengths = sorted(set(r['bits'] for r in results))
    avg_memory = []

    for bits in bit_lengths:
        bit_memory = [r['memory'] for r in results if r['bits'] == bits]
        avg_mem = np.mean(bit_memory)
        avg_memory.append(avg_mem)

    plt.figure(figsize=(10, 6))
    plt.plot(bit_lengths, avg_memory, marker='o', color='green')
    plt.title("Average Peak Memory Usage vs Bit Length")
    plt.xlabel("Bit Length of N")
    plt.ylabel("Average Peak Memory (KB)")
    plt.grid(True)
    plt.savefig("plots/memory_plot.png")
    plt.close()

def plot_success_rate(results):
    """Plot success rate vs bit length."""
    bit_lengths = sorted(set(r['bits'] for r in results))
    success_rates = []

    for bits in bit_lengths:
        bit_successes = [r['success'] for r in results if r['bits'] == bits]
        rate = np.mean(bit_successes) * 100  # percentage
        success_rates.append(rate)

    plt.figure(figsize=(10, 6))
    plt.plot(bit_lengths, success_rates, marker='o', color='red')
    plt.title("Success Rate vs Bit Length")
    plt.xlabel("Bit Length of N")
    plt.ylabel("Success Rate (%)")
    plt.ylim(0, 105)
    plt.grid(True)
    plt.savefig("plots/success_rate_plot.png")
    plt.close()