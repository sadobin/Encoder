#! /bin/python3

from Color import Color
import json


class FileHandler:

    def __init__(self, input_file):

        self.input_file = input_file
        self.lines = []

        self.file_reader()


    def file_writer(self, filename, data):

        with open(filename, 'w') as f:
            f.write( json.dumps( data, indent=4 ) )



    def file_reader(self):

        with open(self.input_file, 'r') as f:
            self.lines += [ l for l in f.read().splitlines() ]


    def get_lines(self):
        return self.lines
