#!/usr/bin/python3

import hash_utilities
import argparse
import sys

def success(value):
	print("%s => %s" % (input_hash, value))

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Crack a hash using a rainbow table")
    parser.add_argument("hash", nargs=1, help="Hash to crack")
    parser.add_argument("-i", "--input", nargs=1, help="Rainbow table file")
    args = parser.parse_args()

    input_hash = args.hash[0]

    rainbow_table = {}
    with open(args.input[0]) as f:
            for line in f:
                    plain, hashed = line.split(" ")
                    rainbow_table[hash_utilities.reduce(hashed.strip())] = plain

    if input_hash in rainbow_table.keys():
            success(rainbow_table[input_hash])
    else:
            word = input_hash
            for i in range(1000):
                    word = hash_utilities.reduce(word)
                    if word in rainbow_table.keys():
                            success(rainbow_table[word])
                            break
                    else:
                            word = hash_utilities.hash(word)
