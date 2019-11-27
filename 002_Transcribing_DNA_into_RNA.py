

def convert_dna_to_rna(dna):
    return dna.replace('T', 'U')


if __name__ == '__main__':
    dna = input("Enter a DNA base string:\n").upper()
    rna = convert_dna_to_rna(dna)
    print(rna)

