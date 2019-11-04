import re

class StrCalculator(object):
    def __init__(self, string):
        if StrCalculator.is_a_string(string):
            self.string = string

    @property
    def add(self):
        if self.string == '':
            return 0

        if any(number < 0 for number in self.string_to_integer(self.string)):
             raise ValueError

        return sum(self.string_to_integer(self.string))
    
    def string_to_integer(self, string):
        list_of_strings = (re.sub(r'[^-0-9]+', ' ', string)).split(' ')
        list_of_numbers = [int(number) for number in list_of_strings \
                if number is not '' and len(number) < 4]
        return list_of_numbers

    def is_a_string(string):
        if type(string) is not str:
            raise ValueError('The value must be a string')
        return True

        
