# Given: Two positive integers k (k≤7) and N (N≤2k).
# In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb.
# Tom has two children in the 1st generation, each of whom has two children, and so on.
# Each organism always mates with an organism having genotype Aa Bb.

# Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's
# family tree (don't count the Aa Bb mates at each level).
# Assume that Mendel's second law holds for the factors.


def mate_pairs(parent1_gene1, parent1_gene2, parent2_gene1, parent2_gene2):

    pairs = []

    for p1g1 in parent1_gene1:
        for p2g1 in parent2_gene1:
            # Iterate over second gene
            for p1g2 in parent1_gene2:
                for p2g2 in parent2_gene2:

                    new_gene1 = sorted(p1g1 + p2g1)
                    new_gene2 = sorted(p1g2 + p2g2)
                    pairs.append((new_gene1, new_gene2))

    # There are two children, so we double the pairs
    return pairs * 2

def calculate_probability_of_offspring(k, N):
    # First generation
    pairs = mate_pairs("Aa", "Bb", "Aa", "Bb")

    for generation in range(int(k) - 1):

        child_pairs = []

        for pair in pairs:
            new_pairs = mate_pairs(pair[0], pair[1], "Aa", "Bb")
            child_pairs.extend(new_pairs)

        pairs = child_pairs


    count = 0
    # Count "Aa Bb" children
    for pair in pairs:
        if pair[0][0] == 'A' and pair[0][1] == 'a' and pair[1][0] == 'B' and pair[1][1] == 'b':
            count = count + 1

    # Divide by total number of children
    probability = count / len(pairs)

    return probability



if __name__ == '__main__':

    raw_input = input("Enter k and N:\n")
    k, N = raw_input.split()

    probability = calculate_probability_of_offspring(k, N)
    print(probability)
