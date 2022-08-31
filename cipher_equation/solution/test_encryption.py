""" This module test funcitonality of encrypt() and decrypt() functions """
import pytest
from .encryption import Cipher


@pytest.mark.parametrize('real_data, expected_encrypted_data, key', [
    ("hi, it is me, how are you? are you ok? can you speak?",
    'ŚīüĒīöäĭĵèĿŗîðŚıùäĥĴĭòūıŅıâãĶĩâŁŁŧâĿŝā¢ħĥİèŋšķðťĲçĥįā',
    'yahyaAbbadi'),
    ("Hola Amigos, How are you?", 'ìĹĶĻâåđĳıŉĵÐÄĒĹőâąĖįêœıęã', 'ReemaR')
    ])
def test_encrypt(real_data, expected_encrypted_data, key):
    """ Ensure that encrypt() function encrypt the data correctly
        to be equal the expected real_data string
    Returns:
        bool
    """
    cipher = Cipher(key)
    ecryption_result = cipher.encrypt(real_data)
    assert expected_encrypted_data == ecryption_result


@pytest.mark.parametrize('real_data, encrypted_data, key', [
    ("hi, it is me, how are you? are you ok? can you speak?",
    'ŚīüĒīöäĭĵèĿŗîðŚıùäĥĴĭòūıŅıâãĶĩâŁŁŧâĿŝā¢ħĥİèŋšķðťĲçĥįā',
    'yahyaAbbadi'),
    ("Hola Amigos, How are you?", 'ìĹĶĻâåđĳıŉĵÐÄĒĹőâąĖįêœıęã', 'ReemaR')
    ])
def test_decrypt(real_data, encrypted_data, key):
    """ Ensure that decrypt() method decrypt the data correctly
        to be equal the expected decrypted_data string
    Returns:
        bool
    """
    cipher = Cipher(key)
    decryption_result = cipher.decrypt(encrypted_data)
    assert real_data == decryption_result
