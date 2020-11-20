#! /bin/python3.8

from argparse import ArgumentParser
from Encoder import Encoder

def main():

    parser = ArgumentParser(description="Encoder project cmd arguments")
    parser.add_argument('-A', '--all', help="Encode all characters", action="store_true")
    parser.add_argument('-a', '--append', help="Append users input to the list", action="store_true")
    parser.add_argument('-f', '--file', help="Encode each line in file")
    parser.add_argument('-d', '--desired-chars', help="Characters which will be encoded (MUST be separated by comma[,])")
    parser.add_argument('-x', '--hex', help="Hex format")
    parser.add_argument('-hd', '--html-decimal', help="HTML encoding using ascii in decimal form")
    parser.add_argument('-hx', help="HTML encoding using ascii in hexidecimal form")
    parser.add_argument('-b', '--binary', help="Binary format")
    parser.add_argument('-B', '--base64', help="Base64 format")
    parser.add_argument('-u', '--url', help="URL format")
    parser.add_argument('-U', '--unicode', help="Unicode format")
    args = parser.parse_args()

    try:
        enc = Encoder(args.d, args.f, args.A, args.a)

    except Exception as e:
        print(f"[!] Exception: {e}")


if __name__ == "__main__":
    main()
