# Expected dominant child lookup info
# AA-AA	1.00
# 	-> AA, AA, AA, AA
#
# AA-Aa	1.00
# 	-> AA, Aa, AA, Aa
#
# AA-aa	1.00
# 	-> Aa, Aa, Aa, Aa
#
# Aa-Aa	0.75
# 	-> AA, Aa, aA, aa
#
# Aa-aa	0.5
# 	-> Aa, Aa, aa, aa
#
# aa-aa	0
# 	-> aa, aa, aa, aa

lookup = {
    0: 1.00,
    1: 1.00,
    2: 1.00,
    3: 0.75,
    4: 0.50,
    5: 0.00
}


def get_expected_dominant_children(pop_numbers):

    # Assuming they each have two children
    NUM_CHILDREN = 2

    exp_dom_children = NUM_CHILDREN * (pop_numbers[0] * lookup[0] +
                                       pop_numbers[1] * lookup[1] +
                                       pop_numbers[2] * lookup[2] +
                                       pop_numbers[3] * lookup[3] +
                                       pop_numbers[4] * lookup[4] +
                                       pop_numbers[5] * lookup[5])

    return exp_dom_children


if __name__ == '__main__':

    raw_pop_numbers = input("Enter population numbers:\n")
    split_pop_numbers = raw_pop_numbers.split()
    pop_numbers = [int(n) for n in split_pop_numbers]

    assert len(pop_numbers) == 6

    expected_dominant_children = get_expected_dominant_children(pop_numbers)
    print(expected_dominant_children)

