#! /bin/python3

from FileHandler import FileHandler
from argparse import ArgumentParser
from Encoder import Encoder
from Color import Color

import sys


class Main:

    def __init__(self):

        color = Color()
        self.alert_notation   = color.get('red',   '[!]')
        self.success_notation = color.get('green', '[+]')

        self.args = self.usage()
        self.availables = ['bin', 'hex', 'url', 'html_dec', 'html_hex', 'base64', 'unicode']
        self.schemas = []

        try:
            if not self.args.string and not self.args.file:
                print(f"{ self.alert_notation } No string/file was found.")
                sys.exit(1)

            encoder = Encoder(self.args.string, self.args.desired, self.args.file, self.args.all)
            self.handle_result(encoder)

        except Exception as e:
            print(f"{self.alert_notation} Exception: {e}")
            sys.exit(1)

    
    def usage(self):

        parser = ArgumentParser(description="Encoder project cmd arguments")

        parser.add_argument('string',            help="Input string", nargs="?")
        parser.add_argument('-A',                help="Print all encoding schema for the given input(s)", action="store_true")
        parser.add_argument('-a',  '--all',      help="Encode all characters", action="store_true")
        parser.add_argument('-d',  '--desired',  help="Characters which will be encoded", default="")
        parser.add_argument('-f',  '--file',     help="Encode each line in file")
        parser.add_argument('-w',  '--write',    help="Write the result into the encoder.json")
        parser.add_argument('-b',  '--bin',      help="Binary format", action="store_true")
        parser.add_argument('-x',  '--hex',      help="Hex format", action="store_true")
        parser.add_argument('-B',  '--base64',   help="Base64 format", action="store_true")
        parser.add_argument('-u',  '--url',      help="URL format", action="store_true")
        parser.add_argument('-U',  '--unicode',  help="Unicode format", action="store_true")
        parser.add_argument('-hd', '--html-dec', help="HTML encoding using ascii in decimal form", action="store_true")
        parser.add_argument('-hx', '--html-hex', help="HTML encoding using ascii in hexadecimal form", action="store_true")

        return parser.parse_args()


    def handle_result(self, encoder):

        encoder_result = encoder.get_result()
        result = {}
        
        if not self.args.A:

            # Append user defined schemas to the self.schemas from self.args
            for a in self.availables:
                if vars(self.args)[a]:
                    self.schemas.append(a)

            # Add user-defined schemas value to the result
            for line in encoder_result:
                result[line] = {}
                for s in encoder_result[line]:
                    if s in self.schemas:
                        result[line][s] = encoder_result[line][s]

        else:
            result = encoder_result.copy()


        if self.args.write:
            FileHandler().file_writer(self.args.write, result)

        else:

            for line in result:
                print(f"{self.success_notation} String: {line}")

                for k,v in result[line].items():
                    print(f"{self.success_notation} {k.capitalize().replace('_', ' ')}: {v}")
                
                print()


if __name__ == "__main__":
    Main()

