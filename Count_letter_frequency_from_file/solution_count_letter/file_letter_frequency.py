''' This module Reads a file given its path, and counts the frequency of a given letter '''

class LetterFrequency:
    """ Count a given letter's frequency from a given file path """

    def __init__(self, path):
        """
        Construct all the necessary attributes for the LetterFrequency object.

        Parameters
        ----------
            path : str
                the path of the file to be read
        """
        self.path = path
        self.data = None


    def read_file(self):
        """ Read file into self.data attribute """
        try:
            with open(self.path, encoding = 'utf-8') as file:
                self.data = file.read()

        except (FileNotFoundError, IOError, OSError) as error:
            print(f"{type(error)}: {error}")


    def letter_frequency(self, letter):
        """  Count a given letter's frequency
        Args:
            letter: (string)
        Returns:
            letter's frequency: int
        """
        if not self.data:
            return 0
        return self.data.count(letter)
