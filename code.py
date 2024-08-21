def count_nucleotides(dna_sequence):
    """
    Count the frequency of each nucleotide (A, T, C, G) in the given DNA sequence.
    
    Parameters:
    dna_sequence (str): Input DNA sequence consisting of characters A, T, C, and G.
    
    Returns:
    dict: A dictionary with nucleotides as keys (A, T, C, G) and their respective frequencies as values.
    """
    nucleotide_count = {}
    for nucleotide in dna_sequence:
        if nucleotide in nucleotide_count:
            nucleotide_count[nucleotide] += 1
        else:
            nucleotide_count[nucleotide] = 1
    return nucleotide_count

def print_nucleotide_frequencies(nucleotide_count):
    """
    Print the relative frequency of each nucleotide from the input dictionary of counts.
    
    Parameters:
    nucleotide_count (dict): A dictionary with nucleotides as keys (A, T, C, G) and their respective frequencies as values.
    
    Returns:
    None
    """
    print('Nucleotide frequencies:')
    
    total_nucleotides = sum(nucleotide_count.values())  # Calculate the total count of all nucleotides
    for nucleotide, count in nucleotide_count.items():
        relative_frequency = count / total_nucleotides
        print(f"{nucleotide}: {relative_frequency:.4f}")  # Print each nucleotide with its relative frequency, formatted to 4 decimal places

# Example usage:
# Calculate the nucleotide frequencies of the given DNA sequence and then print their relative frequencies.
dna_sequence = 'ATCTGACGCGCGCCGC'
nucleotide_count = count_nucleotides(dna_sequence)
print_nucleotide_frequencies(nucleotide_count)
