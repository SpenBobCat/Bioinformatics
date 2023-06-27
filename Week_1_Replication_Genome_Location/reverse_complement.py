# By: Michael Spencer

def reverse_complement(sequence):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    reverse_seq = sequence[::-1]
    reverse_complement_seq = ''.join(complement.get(base, base) for base in reverse_seq)
    return reverse_complement_seq

# Example usage
sequence = 'GATTACA'
reverse_comp = reverse_complement(sequence)
print("Reverse Complement:", reverse_comp)
