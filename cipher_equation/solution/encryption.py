""" this module is a cipher implementation of both encryption and decryption"""
import numbers

class Cipher:
    """ Encrypt and decrypt a given string data"""

    def __init__(self, key):
        """
        Construct all the necessary attributes for the Cipher object.

        Parameters
        ----------
            key : str
                A string that will be used symmetrically in encryption and decryption,
                by applying an equation to it with the given data
        """
        self.key = key

    def set_key(self, key):
        """ Add key instance variable """
        self.key = key

    def get_key(self):
        """ Retrieve key instance variable """
        return self.key

    def check_user_input(self, input_data):
        """ Check input data type and convert it into a list of decimals
        Args:
            input (string)
        Returns:
            list: decimal numbers
        """
        if isinstance(input_data, numbers.Number):
            print("Input can't be of number type")
            raise ValueError("Input can't be of number type")
        return [ord(element) for element in input_data]


    def get_key_index(self, data_index, key_index):
        """ return key index incremented by 1 or 0
        Args:
            key_index (int)
            data_index (int)
        Returns:
            int: key index
        """

        if data_index % len(self.get_key()):
            return key_index + 1

        return 0


    def encrypt(self, data):
        """ Convert data into a cipher
        Args:
            data (string): the real data needed to be encrypted
        Returns:
            str: Encrypted data
        """

        # Convert each character into a decimal number
        key2 = self.check_user_input(self.key)
        data = self.check_user_input(data)

        encrypted = ""

        key_index = 0
        for index_data, element_data in enumerate(data):
            key_index = self.get_key_index(index_data, key_index)
            encrypted += (chr( (key2[key_index] << 1) + element_data ))

        return encrypted


    def decrypt(self, encrypted_data):
        """ Decode encrypted data into a human readable intelligible data
        Args:
            encrypted_data (string): the encrypted data needed to be decoded
        Returns:
            str: Decrypted data
        """

        # Convert each character into a decimal number
        key2 = self.check_user_input(self.key)
        encrypted_data = self.check_user_input(encrypted_data)

        decrypted = ""

        key_index = 0
        for index_data, element_data in enumerate(encrypted_data):
            key_index = self.get_key_index(index_data, key_index)
            decrypted += (chr( element_data - (key2[key_index] << 1) ))

        return decrypted
