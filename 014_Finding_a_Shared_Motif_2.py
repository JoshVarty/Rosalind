import numpy as np
from utils import load_fasta_file_as_lookup

# My previous solution used a locally-grow, artisinal SuffixTree to solve the problem.
# While this approach technically worked, it was far from the optimized approaches that others took.
# It's probably worth our time to redo this problem and learn a little bit about dynamic programming.

def find_longest_common_substring_between_two_strings(s1, s2):

    matrix = np.zeros((len(s1), len(s2)))

    max_so_far = 0
    max_strings = []

    for i in range(len(s1)):
        for j in range(len(s2)):

            char1 = s1[i]
            char2 = s2[j]

            if char1 == char2 and (j == 0 or i == 0):
                matrix[i][j] = 1
            elif char1 == char2:
                matrix[i][j] = matrix[i - 1][j - 1] + 1

            # If this string is bigger than the max we've seen, clear all strings
            # as we're about to replace them
            if matrix[i][j] > max_so_far:
                max_strings = []
                max_so_far = matrix[i][j]

            if matrix[i][j] >= max_so_far:

                string_to_add = ""
                index1 = i
                index2 = j
                while index1 >= 0 and index2 >= 0 and matrix[index1][index2] > 0:
                    string_to_add = s1[index1] + string_to_add

                    index1 = index1 - 1
                    index2 = index2 - 1

                max_strings.append(string_to_add)

    return max_so_far, max_strings


def find_longest_common_substring(records):

    global_max = 0
    global_longest = []

    for name, record in records.items():

        if len(global_longest) == 0:
            global_longest.append(record)
            continue

        max_so_far = 0
        longest = []
        for substring in global_longest:

            max, substrings = find_longest_common_substring_between_two_strings(substring, record)

            if max > max_so_far:
                max_so_far = max
                longest = substrings

        global_max = max_so_far
        global_longest = longest

    return global_max, global_longest


if __name__ == '__main__':

    fasta_record_lookup = load_fasta_file_as_lookup('problem_10_data.txt')
    longest_common_substring = find_longest_common_substring(fasta_record_lookup)
    print(longest_common_substring)
