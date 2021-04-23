#! /bin/python3

from Color import Color
import json


class FileHandler:

    def __init__(self):

        self._lines = []


    def file_writer(self, filename, data):

        with open(filename, 'w') as f:
            f.write( json.dumps( data, indent=4 ) )


    def file_reader(self, filename):

        with open(filename, 'r') as f:
            self._lines += [ l for l in f.read().splitlines() ]


    def get_lines(self):
        return self._lines
