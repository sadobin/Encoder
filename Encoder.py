#! /bin/python3.8

from sys import argv


class Encoder:

    def __init__(self, string, desired_list=None, _all=False, file=None):
        self.origin_str = string
        self.hex_str = ''
        self.bin_str = ''
        self.url_str = ''
        self.html_str = ''
        self.html_hex_str = ''
        self.unicode_str = ''
        self.base64_str = ''

        self.list = ['\'', '"', '%', '<', '>', '/']
        if desired_list: self.list += [i for i in desired_list]
        if _all: self.list += [i for i in self.origin_str]


        for char in self.origin_str:
            if char in self.list:
                html_template = '&#_TEXT_;'
                unicode_template = r'\u00_HEX_'

                # Contain hex value of current character
                hx = self.char2hex(char)

                self.hex_str += hx
                self.bin_str += self.hex2bin(hx[0]) + self.hex2bin(hx[1])
                self.url_str += f'%{hx}'
                self.html_str += html_template.replace( '_TEXT_', str(ord(char)) )
                self.html_hex_str += html_template.replace( '_TEXT_', f'x{hx}' )
                self.unicode_str += unicode_template.replace( '_HEX_', hx )
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
        binary = self.bin_str

        # Padding with 0
        remainer = len(binary) % 6
        binary += (6 - remainer) * '0'

        # Spilt into 6-bit group and padding with =
        six_bit_group = [binary[i:i+6] for i in range(0, len(binary), 6)]
        remainer = len(six_bit_group) % 4
        encoding_value = [int(i, base=2) for i in six_bit_group]

        for num in encoding_value:
            if num <= 25:
                self.base64_str += chr(num+65)
            else:
                self.base64_str += chr(num+71)


        #six_bit_group += (4 - remainer) * '='


try:
    o = Encoder(argv[1], _all=True)
    print(o.origin())
    print(o.hex())
    print(o.url())
    print(o.unicode())
    print(o.html_decimal())
    print(o.html_hex())
    print(o.bin())

except Exception as e:
    print(e)
