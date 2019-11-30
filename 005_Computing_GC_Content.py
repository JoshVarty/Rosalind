

def get_gc_content(record):

    # Parse out the name and value based on the first newline
    name = record[:record.index('\n')]
    record_val = record[record.index('\n') + 1:]

    # Count G's, C's and newlines
    g_count = record_val.count("G")
    c_count = record_val.count("C")
    newline_count = record_val.count("\n")

    gc_sum = g_count + c_count
    gc_content = gc_sum / (len(record_val) - newline_count)

    return name, gc_content


def get_highest_gc_content(records):

    split_records = records.split(">")
    split_records = list(filter(None, split_records))  # Remove empty entries

    highest_so_far = -1
    highest_name = ""

    for record in split_records:
        name, gc_content = get_gc_content(record)
        print(name, gc_content)

        if gc_content > highest_so_far:
            highest_name = name
            highest_so_far = gc_content

    return highest_name, highest_so_far


if __name__ == '__main__':

    with open('problem_5_data.txt', 'r') as file:
        fast_a_records = file.read()
        highest_gc_name, highest_gc_value = get_highest_gc_content(fast_a_records)

        print(highest_gc_name)
        print("{:.6f}".format(highest_gc_value * 100))

        # Rosalind_0509
        # 0.532258064516129
