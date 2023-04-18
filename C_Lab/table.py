import time
import random

#Kodexempel - Rabin-Karp:
def rabin_karp(text, pattern):
    d=256
    q=4294967311
    n, m = len(text), len(pattern)
    h = pow(d, m - 1) % q
    p, t = 0, 0

    for i in range(m): 
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for s in range(n - m + 1):
        if p == t:
            if text[s:s + m] == pattern:
                return s

        if s < n - m:
            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q

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

def measure_execution_time(func,element,length,repetitions=10):
    total_time = 0
    for i in range(repetitions):
        pattern = generate_random_pattern(element)
        text = generate_dna_string(length, pattern)
        start_time = time.time()
        func(text, pattern)
        end_time = time.time()
        total_time += (end_time - start_time) * 1000  # time in milliseconds
    return total_time / repetitions

def generate_random_pattern(length):
    return ''.join(random.choice('ACGT') for _ in range(length))

def main():
    # DNA sequences of up to several million nucleotides in length
    text_lengths = [1000000,2500000, 5000000]
    pattern_lengths=[5,10,20,50,100,250,500,1000]

    print("{:<15} {:<15} {:<25} {:<25}".format("Text Length", "Pattern Length", "Rabin-Karp Time (ms)", "Naive Search Time (ms)"))
    
    for element in pattern_lengths:
        for length in text_lengths:
        
            rabin_karp_time = measure_execution_time(rabin_karp,element,length)
            naive_search_time = measure_execution_time(naive_search,element,length)

            print("{:<15} {:<15} {:<25} {:<25}".format(length, element, rabin_karp_time, naive_search_time))

if __name__ == "__main__":
    main()
