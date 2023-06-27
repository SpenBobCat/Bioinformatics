# By: Michael Spencer

def pattern_matching(text, pattern):
    positions = []
    pattern_length = len(pattern)
    text_length = len(text)

    for i in range(text_length - pattern_length + 1):
        if text[i:i+pattern_length] == pattern:
            positions.append(i)

    return positions

# Example usage
text = 'ATGACTTCGCTGTTACGCGC'
pattern = 'CGC'
matches = pattern_matching(text, pattern)
matches_str = ' '.join(str(pos) for pos in matches)
print(matches_str)
