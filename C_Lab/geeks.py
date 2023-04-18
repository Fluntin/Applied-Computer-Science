import time
import random

def rabin_karp(text, pattern):
    n = len(pattern)
    m = len(text)
    q = 101  # A large prime number
    d = 4  # Size of the DNA alphabet (ACGT)
    h = pow(d, m-1) % q

    if m > n:
        return None

    # Convert the DNA sequences to arrays of integers using a mapping of ACGT to 0-3
    dna_map = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    p = [dna_map[c] for c in pattern]
    t = [dna_map[c] for c in text[:m]]

    # Calculate the hash value of the pattern and the first substring of the text
    p_hash = sum([p[i] * pow(d, m-1-i) for i in range(m)]) % q
    t_hash = sum([t[i] * pow(d, m-1-i) for i in range(m)]) % q

    # Matching
    for s in range(n - m + 1):
        # Check if the hash values match
        if p_hash == t_hash:
            # Check if the pattern matches the substring
            if pattern == text[s:s+m]:
                return s
        # Calculate the hash value of the next substring using rolling hash
        if s < n - m:
            t_hash = (d * (t_hash - t[s] * h) + t[(s+m)%n]) % q
            t[s%m] = dna_map[text[(s+m)%n]]

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

def measure_execution_time(func,element,length,repetitions=1000):
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
    text_lengths = [1000,5000,100000,500000,1000000,2500000]
    pattern_lengths=[50,100,250,500,1000]

    print("{:<15} {:<15} {:<25} {:<25}".format("Text Length", "Pattern Length", "Rabin-Karp Time (ms)", "Naive Search Time (ms)"))
    
    for element in pattern_lengths:
        for length in text_lengths:
        
            rabin_karp_time = measure_execution_time(rabin_karp,element,length)
            naive_search_time = measure_execution_time(naive_search,element,length)

            print("{:<15} {:<15} {:<25} {:<25}".format(length, element, rabin_karp_time, naive_search_time))

if __name__ == "__main__":
    main()