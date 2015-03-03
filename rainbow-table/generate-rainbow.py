#!/usr/bin/python3

import sys
import string
import itertools
import hash_utilities
import time
import argparse

def parse_alphabet(alphabet_input):

    return_value = ""
    for elem in [string.ascii_lowercase, string.ascii_uppercase, string.digits]:
        for c in alphabet_input:
            if c in elem:
                return_value += elem
                break
    
    if not return_value:
        print("[Error] unexcepted alphabet")
        sys.exit(1)
    else:
        return return_value


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Generate a rainbow table")
    parser.add_argument("-s", "--size", required=True, nargs=1, help="Size of the alphabet")
    parser.add_argument("-a", "--alphabet", required=True, nargs=1, help="Alphabet")
    parser.add_argument("-o", "--output", required=True, nargs=1, help="Rainbow table file")
    args = parser.parse_args()

    alphabet_size = int(args.size[0])
    alphabet = parse_alphabet(args.alphabet[0])

    print(alphabet)
    with open(args.output[0], "w") as file_out:

        print("0/%s" % alphabet_size)
        for i in range(alphabet_size):

            start_time = time.time()
            for c in itertools.product(alphabet, repeat=(i+1)):
                word = ''.join(c)
                file_out.write("%s " % word)

                for j in range(1000):
                    hash_string = hash_utilities.reduce(hash_utilities.hash(word))
                file_out.write("%s\n" % hash_string)
            
            print("%s/%s [ %s ]" % (i+1, alphabet_size, time.time() - start_time))
