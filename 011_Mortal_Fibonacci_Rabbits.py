# Given: Positive integers n≤100 and m≤20.
# n = number of months
# m = lifespan of rabbits


adult_lookup = {}
baby_lookup = {}


def get_rabbit_pairs(n, m):

    # initialize lookup for negative numbers, 0 and 1
    for i in range(m):
        i = i * -1;
        adult_lookup[i] = 0
        baby_lookup[i] = 0

    adult_lookup[1] = 0
    baby_lookup[1] = 1

    # Build the lookup from the bottom-up
    for i in range(2, n + 1, 1):

        baby_lookup[i] = adult_lookup[i - 1]
        adult_lookup[i] = baby_lookup[i - 1] + adult_lookup[i - 1] - baby_lookup[i - m]

    # Return the total number of babies and adults at time n
    return baby_lookup[n] + adult_lookup[n]


if __name__ == '__main__':

    while True:
        raw_input = input("Enter n and m:\n")
        n, m = raw_input.split()
        n = int(n)
        m = int(m)

        lookup = {}
        number_of_pairs = get_rabbit_pairs(n, m)
        print(number_of_pairs)
