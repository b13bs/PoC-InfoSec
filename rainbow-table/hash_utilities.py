#!/usr/bin/python3

import hashlib

def reduce(input):
	return ''.join(c for c in input if c.isdigit())[:8]

def hash(input):
	return hashlib.sha1(input.encode("utf-8")).hexdigest()
