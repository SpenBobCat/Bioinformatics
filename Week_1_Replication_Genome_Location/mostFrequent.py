# By: Michael Spencer

def most_frequent_3mers(string):
    k = 3  # Length of the desired substring
    kmer_counts = {}

    # Count occurrences of each k-mer
    for i in range(len(string) - k + 1):
        kmer = string[i:i+k]
        if kmer in kmer_counts:
            kmer_counts[kmer] += 1
        else:
            kmer_counts[kmer] = 1

    # Find the maximum frequency
    max_frequency = max(kmer_counts.values())

    # Find all 3-mers with the maximum frequency
    most_frequent_kmers = [kmer for kmer, count in kmer_counts.items() if count == max_frequency]

    return most_frequent_kmers

# Example usage
string = 'TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT'
most_frequent = most_frequent_3mers(string)
print(most_frequent)
