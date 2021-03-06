#! /bin/python3.8

from argparse import ArgumentParser
from Encoder import Encoder
from Color import Color


class Main:

    def __init__(self):

        parser = ArgumentParser(description="Encoder project cmd arguments")
        parser.add_argument('string',            help="Input string")
        parser.add_argument('-a',  '--all',      help="Encode all characters",          action="store_true")
        parser.add_argument('-f',  '--file',     help="Encode each line in file")
        parser.add_argument('-d',  '--desired',  help="Characters which will be encoded (MUST be separated by comma[,])", default="")
        parser.add_argument('-hd', '--html-dec', help="HTML encoding using ascii in decimal form",     action="store_true")
        parser.add_argument('-hx', '--html-hex', help="HTML encoding using ascii in hexadecimal form", action="store_true")
        parser.add_argument('-b',  '--bin',      help="Binary format",  action="store_true")
        parser.add_argument('-x',  '--hex',      help="Hex format",     action="store_true")
        parser.add_argument('-B',  '--base64',   help="Base64 format",  action="store_true")
        parser.add_argument('-u',  '--url',      help="URL format",     action="store_true")
        parser.add_argument('-U',  '--unicode',  help="Unicode format", action="store_true")
        args = parser.parse_args()


        self.items = {
                        'bin': args.bin,
                        'hex': args.hex,
                        'url': args.url,
                        'html_decimal': args.html_dec,
                        'html_hexadecimal': args.html_hex,
                        'base64': args.base64,
                        'unicode': args.unicode,
                }


        try:
            self.e = Encoder(args.string, args.desired, args.file, args.all)
            self.printer()

        except Exception as e:
            self.printer(e)

    

    def printer(self, error=None):

        color = Color()

        if error:
            alert_mark = color.get('red', '[!]')
            print(f"{alert_mark} Exception: {error}")

        else:
            success_mark = color.get('green', '[+]')
            print(f"{success_mark} String: {self.e.get('string')}")
            
            for item in self.items:
                if self.items[ item ]:
                    print(f"{success_mark} {item.capitalize().replace('_', ' ')} format: {self.e.get(item)}")




main = Main()

