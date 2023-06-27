# By: Michael Spencer

def count_pattern(text, pattern):
    count = 0
    pattern_length = len(pattern)
    text_length = len(text)

    for i in range(text_length - pattern_length + 1):
        if text[i:i+pattern_length] == pattern:
            count += 1

    return count

def count_3mers(text):
    k = 3  # Length of the desired substring
    kmer_counts = {}

    # Count occurrences of each k-mer
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        if kmer in kmer_counts:
            kmer_counts[kmer] += 1
        else:
            kmer_counts[kmer] = 1

    return kmer_counts

# Example usage
text = 'ACTGTACGATGATGTGTGTCAAAG'
pattern = 'TGT'

pattern_count = count_pattern(text, pattern)
print("Count of Pattern:", pattern_count)

frequency = count_3mers(text)
print("Frequency of 3-mer Patterns:")
for kmer, count in frequency.items():
    print(kmer, "-", count)
