#! /bin/python3.8

from sys import argv


class Encoder:

    def __init__(self, string, desired_list=None, all_characters=False):
        self.origin_str = string
        self.hex_str = ''
        self.url_str = ''
        self.html_str = ''
        self.html_hex_str = ''
        self.unicode_str = ''
        self.base64_str = ''

        self.list = ['\'', '"', '%', '<', '>']
        if desired_list: self.list += desired_list 
        if all_characters: self.list += [i for i in self.origin_str]


        for char in self.origin_str:
            if char in self.list:
                html_template = '&#_TEXT_;'
                unicode_template = r'\u00_HEX_'

                self.url_str += f'%{hex(ord(char))[2:]}'
                self.html_str += html_template.replace( '_TEXT_', str(ord(char)) )
                self.html_hex_str += html_template.replace( '_TEXT_', f'x{self.char_hex(char)}' )
                self.unicode_str += unicode_template.replace( '_HEX_', self.char_hex(char) )
            else:
                self.hex_str += self.char_hex(char)
                self.url_str += char
                self.html_str += char
                self.html_hex_str += char
                self.unicode_str += char


    def char_hex(self, char):
        return str(hex(ord(char))[2:])


    def origin(self):
        return self.origin_str


    def url(self):
        return self.url_str


    def hex(self):
        return self.hex_str


    def html_decimal(self):
        return self.html_str


    def html_hex(self):
        return self.html_hex_str


    def unicode(self):
        return self.unicode_str


    def base64(self):
        return self.base64_str



o = Encoder(argv[1], all_characters=True)
print(o.origin())
print(o.hex())
print(o.url())
print(o.unicode())
print(o.html_decimal())
print(o.html_hex())
