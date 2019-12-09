

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

