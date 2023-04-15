#Now, you can create a script that generates the bar chart:
import time
import random
import matplotlib.pyplot as plt




def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    p_hash = hash(pattern)
    for i in range(n - m + 1):
        if hash(text[i:i + m]) == p_hash:
            if text[i:i + m] == pattern:
                print("Found!")
                return i
    return None

def naive_search(text, pattern):
    n, m = len(text), len(pattern)

    for s in range(n - m + 1):
        if text[s:s + m] == pattern:
            return s

    return None

def generate_dna_string(length):
    return ''.join(random.choice('ACGT') for _ in range(length))

def measure_execution_time(func, text, pattern):
    start_time = time.time()
    func(text, pattern)
    end_time = time.time()
    return (end_time - start_time) * 1000  # return time in milliseconds

def plot_execution_times(text_lengths, rabin_karp_times, naive_search_times):
    width = 0.35
    fig, ax = plt.subplots()

    x_axis = [str(length) for length in text_lengths]

    ax.bar(x_axis, rabin_karp_times, width, label='Rabin-Karp')
    ax.bar(x_axis, naive_search_times, width, bottom=rabin_karp_times, label='Naive Search')

    ax.set_xlabel('DNA String Length')
    ax.set_ylabel('Execution Time (ms)')
    ax.set_title('Execution Time Comparison of Rabin-Karp and Naive Search Algorithms')
    ax.legend()

    plt.show()

def main():
    text_lengths = [1000, 5000, 10000, 50000]
    pattern = "AAAGCTTGATGT"

    rabin_karp_times = []
    naive_search_times = []

    for length in text_lengths:
        text = generate_dna_string(length)
        rabin_karp_time = measure_execution_time(rabin_karp, text, pattern)
        naive_search_time = measure_execution_time(naive_search, text, pattern)

        rabin_karp_times.append(rabin_karp_time)
        naive_search_times.append(naive_search_time)

    plot_execution_times(text_lengths, rabin_karp_times, naive_search_times)

if __name__ == "__main__":
    main()