#! /bin/python3.8


class ListHandler:

    def __init__(self, string, desired_chars, File, All, append):

        try:

            self.list = []
            self.suggested_list = ['\'', '"', '%', '<', '>', '/', '\\']

            if All:
                self.list += [ i for i in string ]

            elif desired_chars:
                self.list = [ i for i in desired_chars.split(',') ] + (self.suggested if append else [])

            elif File:
                self.list = self.file_reader(File) + (self.suggested if append else [])

        except:
            pass


    def file_reader(self, File):

        with open(File, 'r') as f:
            lines = []
            lines += [ l for l in f.read().splitlines() ]
            return lines


    def get(self):
        return self.list
