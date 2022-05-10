import numpy as np
import random as rand


# Global varables
# Default alphabets
default_DNA = {base: .25 for base in "ATGC"}
default_AA = {aa: .05 for aa in "ACDEFGHIKLMNPQRSTVWY"}
default_BINARY = {bit: .5 for bit in "10"}


class RandomGenerator:
    alphabet = {}
    counts = []

    def __init__(self, alphabet_dict=None, filepath=None, default_mode="none"):
        default_mode = default_mode.lower()
        if default_mode in "dna":
            self.alphabet = default_DNA
        elif default_mode in ["aa","protien"]:
            self.alphabet = default_AA
        elif default_mode in "binary":
            self.alphabet = default_BINARY
        else:
            if alphabet_dict is None:
                self.alphabet = RandomGenerator._get_alphabet_from_file(filepath)
            elif filepath is None:
                self.alphabet = alphabet_dict
            else:
                raise IOError

        
        counts = [0] * len(alphabet_dict)


    def _generate_multiple_sequence(self, num_sequences, length):
        sequences = []
        for i in range(0, num_sequences):
            sequences.append(self._generate_single_sequence(length))

        return sequences

    # Functions for generating sequences
    def _generate_single_sequence(self, length):
        """
        Generate a single string of length n using the dictionary provided by the user.
        """

        sequence = ""

        for i in range(0,length):
            random_val = rand.random()
            sequence += self._pick_character(random_val)

        return sequence

    def _pick_character(self, random_val):

        """
        This function iterates though the dictionary of characters and frequencies, summing the freqs
        as they appear. The probability that on any loop, random_val < freq_sum[i] is equal to the probability
        that freq_sum[i-1] < random_val < freq_sum[i] = freq of the character in question.
        """
        probability_threshold = 0
        for char, freq in self.alphabet.items():
            probability_threshold += freq
            if random_val < probability_threshold:

                return char


    @staticmethod
    def _get_alphabet_from_file(filepath):
        """
        Reads in a file to create a dictionary compatible with the RandomGenerator object. Keeps a count
        of all values passed through it: this allows for input file to have entries of char:count or char:freq,
        as counts will be converted to freq, and frequencies will be divided by 1.
        TODO: Consider adding a warning message to let the user know if they get a float total_count, in case of input mistake
        :param filepath:
        :param sep:
        :return: alphabet dictionary
        """

        input_file = open(filepath, "r")
        rows = input_file.readlines()
        input_file.close()

        total_count = 0
        char_count_tuples = []
        alphabet = {}

        for row in rows:
            values = row.split()
            char_count_tuples.append((values[0], float(values[1])))
            total_count += float(values[1])

        for char, count in char_count_tuples:
            freq = count/total_count
            alphabet[char] = freq

        return alphabet

# For testing
if __name__ == "__main__":

    coin_flipper = RandomGenerator("input_test.txt")
    print(coin_flipper._generate_single_sequence(10))