import time
import random

def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    p_hash = hash(pattern)
    for i in range(n - m + 1):
        if hash(text[i:i + m]) == p_hash:
            if text[i:i + m] == pattern:
                #print("Found!")
                return i
    return None

def naive_search(text, pattern):
    n, m = len(text), len(pattern)

    for s in range(n - m + 1):
        if text[s:s + m] == pattern:
            return s

    return None

def generate_dna_string(length, pattern):
    dna_string = ''.join(random.choice('ACGT') for _ in range(length))
    insertion_index = random.randint(0, length - len(pattern))
    dna_string = dna_string[:insertion_index] + pattern + dna_string[insertion_index + len(pattern):]
    return dna_string

def measure_execution_time(func, text, pattern, repetitions=10):
    total_time = 0
    for i in range(repetitions):
        start_time = time.time()
        func(text, pattern)
        end_time = time.time()
        total_time += (end_time - start_time) * 1000  # time in milliseconds
    return total_time / repetitions

def generate_random_pattern(length):
    return ''.join(random.choice('ACGT') for _ in range(length))

def main():
    text_lengths = [1000000, 5000000, 1000000, 5000000]
    pattern_lengths=[5,7,10,20,50,100]

    print("{:<15} {:<15} {:<25} {:<25}".format("Text Length", "Pattern Length", "Rabin-Karp Time (ms)", "Naive Search Time (ms)"))
    
    for element in pattern_lengths:
        for length in text_lengths:
        
            pattern = generate_random_pattern(element)
            text = generate_dna_string(length, pattern)
            rabin_karp_time = measure_execution_time(rabin_karp, text, pattern)
            naive_search_time = measure_execution_time(naive_search, text, pattern)

            print("{:<15} {:<15} {:<25} {:<25}".format(length, element, rabin_karp_time, naive_search_time))

if __name__ == "__main__":
    main()
