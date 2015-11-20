#!/usr/bin/env python3

def string_to_number(string):
    return_number = 0
    for idx, char in enumerate(string):
        return_number += (ord(char) * (256**idx))
    return return_number


def number_to_string(number):
    return_string = ""
    
    while True:
        return_string += chr(number % 256)
        number_prec = number // 256
        if number_prec == number:
            break
        else:
            number= number_prec 

    return return_string


chaine = "abc"
a = string_to_number(chaine)
b = number_to_string(a)

for idx,char in enumerate(b):
    print(idx,char,ord(char))

if chaine[:2] == b[:2]:
    print("+++ Tout fonctionne!")
else:
    print("nope")
