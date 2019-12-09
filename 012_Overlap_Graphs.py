from utils import load_fasta_file_as_lookup


def build_adjacency_list(record_lookup, k=3):

    prefix_lookup = {}
    adjacency_list = {}

    # Create a lookup from prefix -> record name
    for prefix_name, dna in record_lookup.items():
        prefix = dna[:k]

        if prefix not in prefix_lookup:
            prefix_lookup[prefix] = []

        prefix_lookup[prefix].append(prefix_name)

    # Match suffixes using the prefix lookup
    for suffix_name, dna in record_lookup.items():

        suffix = dna[-k:]
        if suffix in prefix_lookup:
            prefix_names = prefix_lookup[suffix]

            for prefix_name in prefix_names:

                # Don't match an entry to itself
                if suffix_name != prefix_name:
                    if suffix_name not in adjacency_list:
                        adjacency_list[suffix_name] = []

                    adjacency_list[suffix_name].append(prefix_name)

    return adjacency_list


if __name__ == '__main__':

    fasta_record_lookup = load_fasta_file_as_lookup('problem_12_data.txt')
    adjacency_list = build_adjacency_list(fasta_record_lookup)

    for key, value_list in adjacency_list.items():
        for value in value_list:
            print(key, value)

