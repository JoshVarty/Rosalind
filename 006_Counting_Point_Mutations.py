

def count_point_mutations(dna_1, dna_2):

    assert len(dna_1) == len(dna_2)

    num_point_mutations = 0

    for base_1, base_2 in zip(dna_1, dna_2):

        if base_1 != base_2:
            num_point_mutations = num_point_mutations + 1

    return num_point_mutations


if __name__ == '__main__':

    dna_1 = input("Enter first DNA sequence:\n")
    dna_2 = input("Enter second DNA sequence:\n")

    num_point_mutations = count_point_mutations(dna_1, dna_2)
    print("Number of point mutations:")
    print(num_point_mutations)

