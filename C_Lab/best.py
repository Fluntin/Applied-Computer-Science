# Here's an updated version of the script that incorporates these suggestions:
# To run this script, you need to install the biopython library if you haven't already:
# pip install biopython

import time
import random
import matplotlib.pyplot as plt
import requests
from Bio import SeqIO
from io import StringIO

# ... (include the previous functions here) ...

def get_dna_sequence_from_genbank(accession_number):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id={accession_number}&rettype=fasta&retmode=text"
    response = requests.get(url)
    fasta_data = response.text
    fasta_file = StringIO(fasta_data)
    record = SeqIO.read(fasta_file, "fasta")
    return str(record.seq)

def main():
    text_lengths = [1000, 5000, 10000, 50000]
    pattern = "AAAGCTTTGATGGT"

    rabin_karp_times = []
    naive_search_times = []

    # Test on random DNA sequences
    for length in text_lengths:
        text = generate_dna_string(length)
        rabin_karp_time = measure_execution_time(rabin_karp, text, pattern)
        naive_search_time = measure_execution_time(naive_search, text, pattern)

        rabin_karp_times.append(rabin_karp_time)
        naive_search_times.append(naive_search_time)

    plot_execution_times(text_lengths, rabin_karp_times, naive_search_times)

    # Test on real-world DNA sequence data
    accession_number = "NC_000852"  # Example GenBank accession number
    real_dna_sequence = get_dna_sequence_from_genbank(accession_number)

    rabin_karp_time_real = measure_execution_time(rabin_karp, real_dna_sequence, pattern)
    naive_search_time_real = measure_execution_time(naive_search, real_dna_sequence, pattern)

    print(f"Rabin-Karp execution time on real DNA sequence data: {rabin_karp_time_real} ms")
    print(f"Naive search execution time on real DNA sequence data: {naive_search_time_real} ms")

if __name__ == "__main__":
    main()