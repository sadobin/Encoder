#!/usr/bin/python3.8

# Importing color list 
import os, sys
sys.path.append( os.path.dirname( os.path.dirname(__file__) ) )

from lib.color_list import color_table


class Color:

    def __init__(self):
        global color_table


    def get(self, color, string=None, substr=None, bg=0):

        color += 'bg' if bg else ''

        if color in color_table:

            if substr:
                substr_temp = color_table[ color ].replace('__TEXT__', substr)
                string = string.replace(substr, substr_temp)
            else:
                string = color_table[ color ].replace('__TEXT__', string)


        return string

