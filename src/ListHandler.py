#! /bin/python3.8


class ListHandler:

    def __init__(self, string, desired_chars, File, All):

        self.list = []

        try:
            if All:
                self.list += [ i for i in string ]

            elif desired_chars:
                self.list = [ i for i in desired_chars.split(',') ]

            elif File:
                self.list = self.file_reader(File)

        except:
            pass


    def file_reader(self, File):

        with open(File, 'r') as f:
            lines = []
            lines += [ l for l in f.read().splitlines() ]
            return lines


    def get(self):
        return self.list
