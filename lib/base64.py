#! /bin/python3.8

from sys import argv
import base64_list

table = base64_list.base64_table

def binary(text):

    hx = ''
    bn = ''
    for i in text:
        hx += hex(ord(i))[2:]

    for i in hx:
        bn += bin(int(i, base=16))[2:].zfill(4)

    return bn


def base64(text):

    base64_str = ''
    bin_str = binary(text)

    """
         If Base64 encoded string does not exist,
        perform encoding; otherwise return encoded result
    """

    # Padding with 0
    remainer = len(bin_str) % 6
    if remainer != 0:
        bin_str += (6 - remainer) * '0'

    # Spilt into 6-bit group
    six_bit_group = [bin_str[i:i+6] for i in range(0, len(bin_str), 6)]
    encoded_value = [str(int(i, base=2)) for i in six_bit_group]
    remainer = len(encoded_value) % 4

    # Mapping binary number to its standard format
    for num in encoded_value:
        base64_str += table[ num ]

    # Padding with =
    if remainer != 0:
        base64_str += (4 - remainer) * '='

    # Return encoded result
    return base64_str


try:
    user_input = argv[1]
    temp = base64(user_input)
    print(temp)
except Exception as e:
    print(e)
