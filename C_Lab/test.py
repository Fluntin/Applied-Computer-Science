import time

#Kodexempel - Rabin-Karp:
def rabin_karp(text, pattern, d, q):
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

#---------------------------------------------------------------------

def rabin_karp_alt(text, pattern):
    n, m = len(text), len(pattern)
    p_hash = hash(pattern)
    for i in range(n - m + 1):
        if hash(text[i:i + m]) == p_hash:
            if text[i:i + m] == pattern:
                print("Found!")
                return i
    return None
#---------------------------------------------------------------------

#Kodexempel - Naiv textsökning:
def naive_search(text, pattern):
    n, m = len(text), len(pattern)

    for s in range(n - m + 1):
        if text[s:s + m] == pattern:
            return s

    return None
#---------------------------------------------------------------------
Dna="AGCTAGCTACGACTACGACTAGCTAGCTAGCTAGCTACGACTAGCTAGCTAAAAGCTTTGATGGTGCTAGCTACGACTAGCTACGACTACGACTACGACTACGACTAGCTAGCTAGCTACGACTACGACTAGCTAGCTAGCTAGCTAGCTACGACTACGACTACGACTACGACTACGAAAGCTTTGATGGTACTACGACTAGCTAGCTAGCTAGCTACGACTACGACTAGCTAGCTACGACTACGACTAGCTAGCTAGCTACGACTACGACTAGCTACGACTACGACTACGACTAGCTAGCTAGCTACGACTAGCTACGACTAGCTAGCTACGACTACGACTAGCTAGCTAGCTACGACTAGCTAGCTAGCTACGACTAGCTACGACTAGCTAGCTAGCTACGACTACGACTACGACTAGCTACGACTACGACTACGACTAGCTACGACTACGACTAGCTACGACTAGCTACGACTACGACTACGACTAGCTAGCTACGACTAGCTAGCTACGACTAGCTACGACTAGCTAGCTAGCTACGACTAGCTAGCTAGCTACGACTAGCTACGACTAGCTAGCTAGCTACGACTACGACTAGCTAGCTAGCTACGACTACGACTAGCTAGCTAGCTAGCTACGACTACGACTAGCTAGCTAGCTACGACTAGCTACGACTAGCTAGCTACGACTACGACTACGACTAGCTAGCTACGACTACGACTACGACTAGCTAGCTAGCTACGACTACGACTAGCTAGCTAGCTACGACTACGACTACGACTAGCTACGACTACGACTAGCTACGACTACGACTAGCTAGCTAGCTACGACTAGCTAGCTAGCTACGACTAGCTACGACTACGACTAGCTAGCTAGCTACGACTACGACTACGACTACGACTAGCTACGACTACGACTAGCTAGCTACGACTACGACTAGCTAGCTACGACTAGCTAGCTACGACTAGCTACGACTACGACTAGCTACGACTAGCTACGACTACGACTACGACTAGCTAGCTACGACTAGCTAGCTACGACTACGACTACGACTAGCTAGCTAGCTACGACTACGACTACGACTACGACTAGCTACGACTACGACTAGCTAGCTAGCTACGACTACGACTACGACTAGCTACGACTACGACTACGACTAGCTAGCTAGCTACGACTACGACTAGCTACGACTAGCTACGACTAGCTACGACTAGCTACGACTAGCTACGACTAGCTACGACTACGACTACGACTAGCTACGACTAGCTACGACTAGCTAGCTAGCTACGACTACGACTAGCTACGACTACGACTAGCTACGACTACGACTACGACTAGCTAGCTAGCTACGACTACGACTACGACTAGCTAGCTAGCTACGACTACGACTACGACTAGCTACGACTACGACTACGACTAGCTAGCTACGACTAGCTAGCTACGACTACGACTACGACTAGCTAGCTAGCTACGACTACGACTAGCTACGACT"
Sequence="AAAGCTTTGATGGT"
#---------------------------------------------------------------------
start_time = time.time()
print(rabin_karp_alt(Dna,Sequence))
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
#---------------------------------------------------------------------
start_time = time.time()
print(naive_search(Dna,Sequence))
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")