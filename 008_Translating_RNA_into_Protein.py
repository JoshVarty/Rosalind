
# UUU F      CUU L      AUU I      GUU V
# UUC F      CUC L      AUC I      GUC V
# UUA L      CUA L      AUA I      GUA V
# UUG L      CUG L      AUG M      GUG V
# UCU S      CCU P      ACU T      GCU A
# UCC S      CCC P      ACC T      GCC A
# UCA S      CCA P      ACA T      GCA A
# UCG S      CCG P      ACG T      GCG A
# UAU Y      CAU H      AAU N      GAU D
# UAC Y      CAC H      AAC N      GAC D
# UAA Stop   CAA Q      AAA K      GAA E
# UAG Stop   CAG Q      AAG K      GAG E
# UGU C      CGU R      AGU S      GGU G
# UGC C      CGC R      AGC S      GGC G
# UGA Stop   CGA R      AGA R      GGA G
# UGG W      CGG R      AGG R      GGG G


lookup = {
    'UUU': 'F',
    'CUU': 'L',
    'AUU': 'I',
    'GUU': 'V',
    'UUC': 'F',
    'CUC': 'L',
    'AUC': 'I',
    'GUC': 'V',
    'UUA': 'L',
    'CUA': 'L',
    'AUA': 'I',
    'GUA': 'V',
    'UUG': 'L',
    'CUG': 'L',
    'AUG': 'M',
    'GUG': 'V',
    'UCU': 'S',
    'CCU': 'P',
    'ACU': 'T',
    'GCU': 'A',
    'UCC': 'S',
    'CCC': 'P',
    'ACC': 'T',
    'GCC': 'A',
    'UCA': 'S',
    'CCA': 'P',
    'ACA': 'T',
    'GCA': 'A',
    'UCG': 'S',
    'CCG': 'P',
    'ACG': 'T',
    'GCG': 'A',
    'UAU': 'Y',
    'CAU': 'H',
    'AAU': 'N',
    'GAU': 'D',
    'UAC': 'Y',
    'CAC': 'H',
    'AAC': 'N',
    'GAC': 'D',
    'UAA': 'Stop',
    'CAA': 'Q',
    'AAA': 'K',
    'GAA': 'E',
    'UAG': 'Stop',
    'CAG': 'Q',
    'AAG': 'K',
    'GAG': 'E',
    'UGU': 'C',
    'CGU': 'R',
    'AGU': 'S',
    'GGU': 'G',
    'UGC': 'C',
    'CGC': 'R',
    'AGC': 'S',
    'GGC': 'G',
    'UGA': 'Stop',
    'CGA': 'R',
    'AGA': 'R',
    'GGA': 'G',
    'UGG': 'W',
    'CGG': 'R',
    'AGG': 'R',
    'GGG': 'G'
}


def convert_rna_to_protein(rna_sequence):

    protein_list = []

    for i in range(0, len(rna_sequence), 3):

        codon = rna_sequence[i:i+3]
        protein = lookup[codon]

        if protein != 'Stop':
            protein_list.append(protein)

    protein_sequence = ''.join(protein_list)
    return protein_sequence



if __name__ == '__main__':

    rna_sequence = input("Enter RNA sequence:\n")
    protein_sequence = convert_rna_to_protein(rna_sequence)

    print(protein_sequence)
