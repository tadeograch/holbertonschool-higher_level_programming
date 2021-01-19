#!/usr/bin/python3
'''My list class'''


class MyList(list):
    '''Inherits from list class'''
    def print_sorted(self):
        '''Print the list sorted'''
        print(sorted(self))
