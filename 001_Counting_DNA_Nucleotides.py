

def count_bases(dna):

    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0

    for base in dna:
        if base == 'a':
            a_count = a_count + 1
        elif base == 'c':
            c_count = c_count + 1
        elif base == 'g':
            g_count = g_count + 1
        elif base == 't':
            t_count = t_count + 1
        else:
            raise Exception("DNA should consist of A, C, G and T bases. Found: {}".format(base))

    return a_count, c_count, g_count, t_count


if __name__ == '__main__':
    dna = input("Enter a DNA base string:\n").lower()
    a_count, c_count, g_count, t_count = count_bases(dna)

    print(a_count)
    print(c_count)
    print(g_count)
    print(t_count)



