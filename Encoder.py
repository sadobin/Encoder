#! /bin/python3.8

from sys import argv
from argparse import ArgumentParser

table = {
'0': 'A',
'1': 'B',
'2': 'C',
'3': 'D',
'4': 'E',
'5': 'F',
'6': 'G',
'7': 'H',
'8': 'I',
'9': 'J',
'10': 'K',
'11': 'L',
'12': 'M',
'13': 'N',
'14': 'O',
'15': 'P',
'16': 'Q',
'17': 'R',
'18': 'S',
'19': 'T',
'20': 'U',
'21': 'V',
'22': 'W',
'23': 'X',
'24': 'Y',
'25': 'Z',
'26': 'a',
'27': 'b',
'28': 'c',
'29': 'd',
'30': 'e',
'31': 'f',
'32': 'g',
'33': 'h',
'34': 'i',
'35': 'j',
'36': 'k',
'37': 'l',
'38': 'm',
'39': 'n',
'40': 'o',
'41': 'p',
'42': 'q',
'43': 'r',
'44': 's',
'45': 't',
'46': 'u',
'47': 'v',
'48': 'w',
'49': 'x',
'50': 'y',
'51': 'z',
'52': '0',
'53': '1',
'54': '2',
'55': '3',
'56': '4',
'57': '5',
'58': '6',
'59': '7',
'60': '8',
'61': '9',
'62': '+',
'63': '/',
}


class Encoder:

    def __init__(self, string, desired_chars=None, _all=False, file=None):
        global table
        self.origin_str = string
        self.hex_str = ''
        self.bin_str = ''
        self.url_str = ''
        self.html_str = ''
        self.html_hex_str = ''
        self.unicode_str = ''
        self.base64_str = ''

        self.list = ['\'', '"', '%', '<', '>', '/', '\\']
        if desired_chars: self.list += [i for i in desired_chars]
        if _all: self.list += [i for i in self.origin_str]


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
        return self.hex_str


    def bin(self):
        return self.bin_str


    def html_decimal(self):
        return self.html_str


    def html_hex(self):
        return self.html_hex_str


    def unicode(self):
        return self.unicode_str


    # Implementation of Base64 encoding
    def base64(self):

        """
             If Base64 encoded string does not exist,
            perform encoding; otherwise return encoded result
        """
        if not self.base64_str:

            binary = self.bin_str

            # Padding with 0
            remainer = len(binary) % 6
            binary += (6 - remainer) * '0'

            # Spilt into 6-bit group
            six_bit_group = [binary[i:i+6] for i in range(0, len(binary), 6)]
            encoded_value = [str(int(i, base=2)) for i in six_bit_group]

            # Mapping binary number to its standard format
            for num in encoded_value:
                if num in table:
                    index = encoded_value.index(num)
                    encoded_value[ index ] = table[num]

            # Padding with =
            remainer = len(encoded_value) % 4
            encoded_value += (3 - remainer) * '='

            for i in encoded_value:
                self.base64_str += i

        # Return encoded result
        return self.base64_str


try:
    o = Encoder(argv[1], _all=True)
    print(f'[+] Print origin:\n{o.origin()}')
    print(f'[+] Print hex:\n{o.hex()}')
    print(f'[+] Print url:\n{o.url()}')
    print(f'[+] Print unicode:\n{o.unicode()}')
    print(f'[+] Print html_decimal:\n{o.html_decimal()}')
    print(f'[+] Print html_hex:\n{o.html_hex()}')
    print(f'[+] Print bin:\n{o.bin()}')
    print(f'[+] Print base64:\n{o.base64()}')

except Exception as e:
    print(e)
