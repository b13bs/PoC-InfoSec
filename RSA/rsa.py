#!/usr/bin/python3

import random
from pprint import pprint
import os
import codecs
import fractions
import binascii
import json

def phi(n):
    amount = 0

    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1

    return amount


with open("primes.txt") as f:
    lines = f.readlines()
    p1 = int(random.choice(lines).strip())
    p2 = int(random.choice(lines).strip())


def generate_keys():
    n = p1*p2
    phi_n = (p1-1) * (p2-1)

    # choisir e, prime relative à phi_n (phi_n peut pas être divisable par e)
    for i in range(100):
        e = i+2
        if not (phi_n/e).is_integer():
            break

    # computer d
    for i in range(100):
        k = i+1+1
        d = (k * phi_n + 1)/e
        if d.is_integer():
            d = int(d)
            break

    keys = {"p1": p1, "p2": p2, "n": n, "phi_n": phi_n, "e": e, "k": k, "d": d}
    json.dump(keys, open("keys", "w"))

    return (n, e, d)

def load_keys():
    keys = json.load(open("keys"))
    return (keys["n"], keys["e"], keys["d"])

def encrypt(msg, e, n):
    return (msg**e) % n

def string_to_int(chaine):
    return int(codecs.encode(chaine.encode(), "hex"), 16)

def int_to_string(integer):
    return codecs.decode(hex(integer)[2:].encode(), "hex").decode()

def decrypt(encrypted_msg, d, n):
    return (encrypted_msg**d) % n


if __name__ == "__main__":
    if not os.path.isfile("keys"):
        n, e, d = generate_keys()
    else:
        n, e, d = load_keys()

    print("n: %s\ne: %s\nd: %s" % (n,e,d))

    SECRET = 5555
    print("secret: %s" % SECRET)
    encrypted_msg = encrypt(SECRET, e, n)
    print("encrypted_msg: %s" % encrypted_msg)
    decrypted_msg = decrypt(encrypted_msg, d, n)
    print("decrypted_msg: %s" % decrypted_msg)

    assert (SECRET == decrypted_msg)
