import numpy as np

lookup = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3,
}

def get_profile_and_consensuse_for_dna_strings(dna_matrix):

    consensus = ['A' for _ in range(len(dna_matrix[0]))]
    consensus_max_count = np.zeros((len(dna_matrix[0]),))
    profile_matrix = np.zeros((4, len(dna_matrix[0])), dtype=np.int)

    # Build profile matrix
    for row in range(len(dna_matrix)):
        for col in range(len(dna_matrix[row])):

            base = dna_matrix[row][col]
            index = lookup[base]
            profile_matrix[index, col] = profile_matrix[index, col] + 1

            if profile_matrix[index, col] > consensus_max_count[col]:
                consensus_max_count[col] = profile_matrix[index, col]
                consensus[col] = base

    return profile_matrix, consensus


if __name__ == '__main__':

    with open('problem_10_data.txt', 'r') as file:

        dna_matrix = []
        current_record = ""

        for fast_a_record in file:
            if fast_a_record[0] == '>':
                dna_matrix.append(current_record)
                current_record = ""
            else:
                current_record = current_record + fast_a_record.strip()

        dna_matrix.append(current_record)
        del dna_matrix[0]

        profile, consensus = get_profile_and_consensuse_for_dna_strings(dna_matrix)

        print(''.join(consensus))

        print("A:", ' '.join(map(str, profile[0])))
        print("C:", ' '.join(map(str, profile[1])))
        print("G:", ' '.join(map(str, profile[2])))
        print("T:", ' '.join(map(str, profile[3])))
