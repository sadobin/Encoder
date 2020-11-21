#! /bin/python3.8


# Import ListHandler for better input handling
from ListHandler import ListHandler


# Appending parent directory to the path
import sys
import os
sys.path.append( os.path.dirname( os.path.dirname( os.path.realpath(__file__) ) ) )


# Import base64 table from lib/base64_list.py
from lib.base64_list import base64_table


# Import base64 table
table = base64_table


class Encoder:

    def __init__(self, string, desired_chars=None, File=None, All=False, append=False):

        # Building list of characters which must be encoded
        self.list = ListHandler(string, desired_chars, File, All, append).get()

        global table

        self._result = {
                      "string": string,
                         "hex": "0x",
                         "bin": "",
                         "url": "",
            "html_hexadecimal": "",
                "html_decimal": "",
                     "unicode": "",
                      "base64": "",
                }

        
        # Perform encoding; All characters encoded in binary and hex format 
        for char in self._result['string']:
            if char in self.list:
                html_template = '&#_TEMP_;'
                unicode_template = r'\u00_TEMP_'

                # Hex value of current character
                x = self.char2hex(char)

                self._result['hex']      += x
                self._result['bin']      += self.hex2bin(x[0]) + self.hex2bin(x[1])
                self._result['url']      += f'%{x}'
                self._result['html_decimal'] += html_template.replace( '_TEMP_', str(ord(char)) )
                self._result['html_hexadecimal'] += html_template.replace( '_TEMP_', f'x{x}' )
                self._result['unicode']  += unicode_template.replace( '_TEMP_', x )
            else:
                # Hex value of current character
                x = self.char2hex(char)

                self._result['hex']      += x
                self._result['bin']      += self.hex2bin(x[0]) + self.hex2bin(x[1])
                self._result['url']      += char
                self._result['html_decimal'] += char
                self._result['html_hexadecimal'] += char
                self._result['unicode']  += char


        # Base64 encoding
        self.base64()


    # Return hex value of character
    def char2hex(self, char):
        return str(hex(ord(char))[2:])


    # Return binary value of hexadecimal number
    def hex2bin(self, x):
        return str(bin(int(x, base=16))[2:].zfill(4))


    # Implementation of Base64 encoding based on rfc4648
    def base64(self):

        """
             If Base64 encoded string does not exist,
            perform encoding; otherwise return encoded result
        """
        if not self._result['base64']:

            binary = self._result['bin']

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
                self._result['base64'] += table[ num ]

            # Padding with =
            if remainer != 0:
                self._result['base64'] += (4 - remainer) * '='

        # Return encoded result
        return self._result['base64']


    # Getter method
    def get(self, item):
        try:
            return self._result[item]
        except Exception as e:
            return e
