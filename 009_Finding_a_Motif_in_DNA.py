


def find_start_positions_of_substrings(dna_sequence, query_sequence):

    matching_positions = []
    for start_position in range(len(dna_sequence) - len(query_sequence)):

        sub_seq = dna_sequence[start_position:start_position + len(query_sequence)]

        if sub_seq == query_sequence:
            matching_positions.append(str(start_position + 1))

    return " ".join(matching_positions)


if __name__ == '__main__':

    dna_sequence = input("Enter DNA sequence:\n")
    query_sequence = input("Enter query sequence:\n")

    start_positions = find_start_positions_of_substrings(dna_sequence, query_sequence)

    print(start_positions)
