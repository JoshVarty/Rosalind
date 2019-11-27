

def get_complement_dna(dna):
    complement_dna = []

    for base in reversed(dna):

        complement_base = None

        if base == 'A':
            complement_base = 'T'
        elif base == 'C':
            complement_base = 'G'
        elif base == 'G':
            complement_base = 'C'
        elif base == 'T':
            complement_base = 'A'
        else:
            raise Exception("DNA should consist of A, C, G and T bases. Found: {}".format(base))

        complement_dna.append(complement_base)

    return "".join(complement_dna)


if __name__ == '__main__':
    dna = input("Enter a DNA base string:\n").upper()
    dna_complement = get_complement_dna(dna)

    print(dna_complement)
