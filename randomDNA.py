# This is the script that generates an m-length list of n-length sequences and outputs
# them to stdout where they can be piped to a file.

import random as rand
import sys

#Global variables
nucs = ["A", "C", "G", "T"]

def generate_random_reference(numSeq, lenSeq):

    nucs = ["A", "C", "G", "T"]
    nuc_counts = [0, 0, 0, 0]

    for i in range(0, numSeq):
        sequence = ""
        for j in range(lenSeq):
            random = rand.randint(0, 3)
            sequence += nucs[random]
            nuc_counts[random] += 1
        print(sequence)

    total_nucs = sum(nuc_counts)
    nuc_prop = [count/total_nucs for count in nuc_counts]
    prop_dict = {nucs[i]:nuc_prop[i] for i in range(0, len(nucs))}
    return prop_dict


def generate_random_sequence(lenSeq):
    return ''.join([nucs[rand.randint(0, 3)] for i in range(lenSeq)])


if __name__ == '__main__':
    try:
        output_file = sys.argv[1]
        numSeq = int(sys.argv[2])
        lenSeq = int(sys.argv[3])
    except ValueError or IndexError:
        print("Usage: python randomDNA.py (output file) (number of seq.) (length of seq.)")
        exit()

    outfile = open(output_file, "w")
    original_stdout = sys.stdout
    sys.stdout = outfile
    nuc_proportions = generate_random_reference(numSeq, lenSeq)
    sys.stdout = original_stdout
    print(nuc_proportions)

