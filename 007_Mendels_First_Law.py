
# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms:
#   k individuals are homozygous dominant for a factor,
#   m are heterozygous
#   n are homozygous recessive.
#
# Return: The probability that two randomly selected mating organisms will produce an
# individual possessing a dominant allele (and thus displaying the dominant phenotype).
# Assume that any two organisms can mate.

import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

def get_probability_of_dominant_allele(k, m, n):

    # There are six ways to combine our parent population:
    #   1. hom-dom  +   hom-dom
    #   2. hom-dom  +   het
    #   3. hom-dom  +   hom-rec
    #   4. het      +   het
    #   5. het      +   hom-rec
    #   6. hom-rec  +   hom-rec

    # We need to know two things:
    #   1. For each of the six pairings, what are the probability they lead to an offspring with a dominant allele
    #   2. How often the six different pairings occur

    # The first thing is fixed and reproduced below

    hom_dom_and_hom_dom_gives_dom = 1
    hom_dom_and_het_gives_dom = 1
    hom_dom_and_hom_rec_gives_dom = 1

    het_and_het_gives_dom = 0.75
    het_and_hom_rec_gives_dom = 0.5

    hom_rec_and_hom_rec_gives_dom = 0

    # Now we need to calculate how often each combination can occur
    number_of_combinations = ncr((k + m + n), 2)

    p_hom_dom_and_hom_dom   = ncr(k, 2)             / number_of_combinations
    p_hom_dom_and_het       = ncr(k, 1) * ncr(m, 1) / number_of_combinations
    p_hom_dom_and_hom_rec   = ncr(k, 1) * ncr(n, 1) / number_of_combinations

    p_het_and_het           = ncr(m, 2)             / number_of_combinations
    p_het_and_hom_rec       = ncr(m, 1) * ncr(n, 1) / number_of_combinations

    p_hom_rec_and_hom_rec   = ncr(n, 2)             / number_of_combinations

    probability =   p_hom_dom_and_hom_dom * hom_dom_and_hom_dom_gives_dom + \
                    p_hom_dom_and_het * hom_dom_and_het_gives_dom + \
                    p_hom_dom_and_hom_rec * hom_dom_and_hom_rec_gives_dom + \
                    p_het_and_het * het_and_het_gives_dom + \
                    p_het_and_hom_rec * het_and_hom_rec_gives_dom + \
                    p_hom_rec_and_hom_rec * hom_rec_and_hom_rec_gives_dom

    return probability


if __name__ == '__main__':

    raw_input = input("Enter k, m and n:\n")

    split_input = raw_input.split()
    k, m, n = int(split_input[0]), int(split_input[1]), int(split_input[2]),

    probability = get_probability_of_dominant_allele(k,m,n)
    print(probability)