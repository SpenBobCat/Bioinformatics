# By: Michael Spencer

def count_3mers(string):
    k = 3  # Length of the desired substring
    kmer_counts = {}

    # Count occurrences of each k-mer
    for i in range(len(string) - k + 1):
        kmer = string[i:i+k]
        if kmer in kmer_counts:
            kmer_counts[kmer] += 1
        else:
            kmer_counts[kmer] = 1

    return kmer_counts

# Example usage
string = 'CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA'
frequency = count_3mers(string)
print("Frequency of 3-mers:")
most_frequent_3mer = max(frequency, key=frequency.get)
for kmer, count in frequency.items():
    print(kmer, "-", count)
print("Most frequent 3-mer:", most_frequent_3mer)
