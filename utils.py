import numpy as np
import pandas as pd

def load_fasta_file_as_lookup(filepath):
    with open('problem_10_data.txt', 'r') as file:

        lookup = {}

        raw_string = file.read().replace('\n', '')
        split_file = raw_string.split('>')[1:]

        for record in split_file:
            name = record[:13]
            dna = record[13:]
            lookup[name] = dna

    return lookup


class SuffixNode:
    def __init__(self, num_words, value=""):
        self.children = []
        self.value = value
        self.num_words = num_words
        self.visited = np.zeros((self.num_words,))

    def insert_child(self, new_word, word_id):
        # Mark that we can reach this node
        self.visited[word_id] = 1

        # If we only have the "$" token, we're at the end of the word
        if len(new_word) <= 1:
            return

        chosen_child = None
        # Look for a place for this suffix
        for child in self.children:

            if child.value[0] == new_word[0]:
                chosen_child = child
                break

        if chosen_child is not None:
            # No children are suitable for this one, add it as a child
            chosen_child.insert_child(new_word[1:], word_id)
        else:
            # Found the appropriate, add the suffix
            new_node = SuffixNode(self.num_words, new_word[0])
            new_node.insert_child(new_word[1:], word_id)

            self.children.append(new_node)

    def __str__(self):
        return "Val: " + self.value + "\tChildren: " + str(len(self.children))

    def __repr__(self):
        return self.__str__()


class JoshSuffixTree:
    """
    My own attempt at implementing a generalized suffix tree with a partial understanding of what one actually is.
    """

    def __init__(self, words):
        self.words = words
        self.root = SuffixNode(len(words))

        self.build_tree()
        x = 5

    def get_all_suffixes(self, word):
        return ['$'] + [word[-i:] + '$' for i in range(1, len(word) + 1)]

    def build_tree(self):

        for word_id, word in enumerate(self.words):
            suffixes = self.get_all_suffixes(word)

            for suffix in suffixes:
                # Add to tree
                self.root.insert_child(suffix, word_id)
