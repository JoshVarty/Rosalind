import numpy as np
from utils import load_fasta_file_as_lookup
from utils import SuffixNode, JoshSuffixTree
import sys
sys.setrecursionlimit(10**6)


def find_longest_common_substring(records):

    records_list = [v for k,v in records.items()]
    suffix_tree = JoshSuffixTree(records_list)
    return lcs(suffix_tree.root)


def lcs(node: SuffixNode):

    if not np.all(node.visited):
        return ""

    longest_string = ""
    for child in node.children:

        child_string = lcs(child)
        if len(child_string) > len(longest_string):
            longest_string = child_string

    return node.value + longest_string


if __name__ == '__main__':
    fasta_record_lookup = load_fasta_file_as_lookup('problem_10_data.txt')
    longest_common_substring = find_longest_common_substring(fasta_record_lookup)
    print(longest_common_substring)

