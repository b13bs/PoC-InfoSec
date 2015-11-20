#!/usr/bin/env python3

import sys
import random



def egcd(a, b):
	x,y, u,v = 0,1, 1,0
	while a != 0:
		q, r = b//a, b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
	gcd = b
	return gcd, x, y

def modinv(a, m):
	gcd, x, y = egcd(a, m)
	if gcd != 1:
		raise Exception("Modular inverse does not exist")
	else:
		return x % m


with open("primes.txt", "r") as f:
	primes = f.read().split()

# P
p = int(random.choice(primes))

# Q
different = False
while not different:
	q = int(random.choice(primes))
	if q == p:
		different = False
	else:
		different = True

# N et phi_N
n = p*q
phi_n = (p - 1) * (q - 1)

# E
if phi_n > 65537:
	e = 65537
elif phi_n > 257:
	e = 257
elif phi_n > 17:
	e = 17
elif phi_n > 5:
	e = 5
else:
	e = 3

# D
d = modinv(e, phi_n)

print("p: %s" % p)
print("q: %s" % q)
print("d: %s" % d)
print("e: %s" % e)
print("phi_n: %s" % phi_n)
print("n: %s" % n)

m = 133713
print("m: %s" % m)

ciphered = (m**e) % n
print("ciphered: %s" % ciphered)

decrypted = (ciphered**d) % n
print("decrypted: %s" % decrypted)

if decrypted == m:
	print("+++ TOUT FONCTIONNE!")
else:
	print("--- désolé...")
