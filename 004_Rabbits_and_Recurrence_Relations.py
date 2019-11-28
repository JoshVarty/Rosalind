# Given: Positive integers n≤40 and k≤5.

# Return: The total number of rabbit pairs that will be present after n months,
# if we begin with 1 pair and in each generation, every pair of reproduction-age
# rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

# n = number of months
# k = number of pairs after each month

lookup = {}


def get_rabbit_pairs(n, k):

    if n == 0:
        return 0
    elif n == 1:
        return 1

    prev_gen = 0
    prev_prev_gen = 0

    if (n - 1) in lookup:
        prev_gen = lookup[n - 1]
    else:
        prev_gen = get_rabbit_pairs(n - 1, k)
        lookup[n - 1] = prev_gen

    if (n - 2) in lookup:
        prev_prev_gen = lookup[n - 2]
    else:
        prev_prev_gen = get_rabbit_pairs(n - 2, k)
        lookup[n - 2] = prev_prev_gen

    return prev_gen + k * prev_prev_gen


if __name__ == '__main__':

    while True:
        raw_input = input("Enter n and k:\n")
        n, k = raw_input.split()
        n = int(n)
        k = int(k)

        lookup = {}
        number_of_pairs = get_rabbit_pairs(n, k)
        print(number_of_pairs)
