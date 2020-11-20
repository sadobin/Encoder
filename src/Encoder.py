#! /bin/python3.8


# Adding parent directory to the path
import sys
import os
sys.path.append( os.path.dirname( os.path.dirname( os.path.realpath(__file__) ) ) )

# Import base64 table from lib/base64_list.py
from lib.base64_list import base64_table

from ListHandler import ListHandler

# Assign base64_table list to global table list
table = base64_table


class Encoder:

    def __init__(self, string, desired_chars=None, File=None, All=False, append=False):


        self.list = ListHandler(string, desired_chars, File, All, append).get()

        global table
        self.origin_str = string
        self.hex_str = ''
        self.bin_str = ''
        self.url_str = ''
        self.html_str = ''
        self.html_hex_str = ''
        self.unicode_str = ''
        self.base64_str = ''


        for char in self.origin_str:
            if char in self.list:
                html_template = '&#_TEMP_;'
                unicode_template = r'\u00_TEMP_'

                # Contain hex value of current character
                hx = self.char2hex(char)

                self.hex_str += hx
                self.bin_str += self.hex2bin(hx[0]) + self.hex2bin(hx[1])
                self.url_str += f'%{hx}'
                self.html_str += html_template.replace( '_TEMP_', str(ord(char)) )
                self.html_hex_str += html_template.replace( '_TEMP_', f'x{hx}' )
                self.unicode_str += unicode_template.replace( '_TEMP_', hx )
            else:
                self.hex_str += self.char2hex(char)
                self.url_str += char
                self.html_str += char
                self.html_hex_str += char
                self.unicode_str += char


    def char2hex(self, char):
        return str(hex(ord(char))[2:])


    def hex2bin(self, x):
        return str(bin(int(x, base=16))[2:].zfill(4))


    def origin(self):
        return self.origin_str


    def url(self):
        return self.url_str


    def hex(self):
        return f"0x{self.hex_str}"


    def bin(self):
        return self.bin_str


    def html_decimal(self):
        return self.html_str


    def html_hex(self):
        return self.html_hex_str


    def unicode(self):
        return self.unicode_str


    # Implementation of Base64 encoding based on rfc4648
    def base64(self):

        """
             If Base64 encoded string does not exist,
            perform encoding; otherwise return encoded result
        """
        if not self.base64_str:

            binary = self.bin_str

            # Padding with 0
            remainer = len(binary) % 6
            if remainer != 0:
                binary += (6 - remainer) * '0'

            # Spilt into 6-bit group
            six_bit_group = [binary[i:i+6] for i in range(0, len(binary), 6)]
            encoded_value = [str(int(i, base=2)) for i in six_bit_group]
            remainer = len(encoded_value) % 4

            # Mapping binary number to its standard format
            for num in encoded_value:
                self.base64_str += table[ num ]

            # Padding with =
            if remainer != 0:
                self.base64_str += (4 - remainer) * '='

        # Return encoded result
        return self.base64_str

