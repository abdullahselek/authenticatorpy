#!/usr/bin/env python

import sys
import base64
import time
import hashlib
import binascii
import re

class Authenticator(object):
    """Authenticator class which generates unique one
    time use password.
    """

    def __init__(self, secret):
        """Returns a Authenticator instance.
        Args:
          secret (str):
            User secret which is used in generating one
            time password.
        """

        self._secret = secret
        self.__check_secret(secret)

    def __is_ascii(self, secret):
        return all(ord(c) < 128 for c in secret)

    def __is_alpha(self, secret):
        return all(c.isalpha() for c in secret)

    def __check_secret(self, secret):
        if isinstance(secret, str) == False:
            raise TypeError('You must set a str variable as secret!')
        if self.__is_ascii(secret) == False:
            raise TypeError('You must set an ascii str variable as secret!')
        secret_without_spaces = self.remove_spaces(secret)
        self._secret = self.to_upper_case(secret_without_spaces)
        secret_length = len(self._secret)
        if secret_length < 8:
            raise ValueError('You must set a secret of minimum 8 characters!')
        if secret_length > 8:
            index = secret_length % 8
            self._secret = self._secret[:-index]
        if self.__is_alpha(self._secret) == False:
            raise TypeError('All characters in the secret must be alphabetic!')

    def remove_spaces(self, secret):
        """Returns a new string including no space.
        Args:
          secret (str):
            User secret which is used in generating one
            time password.
        """

        secret_without_spaces = secret.replace(' ', '')
        secret_without_spaces = re.sub(r'\W', '', secret_without_spaces)
        return secret_without_spaces

    def to_upper_case(self, secret_without_spaces):
        """Returns a new string in uppercase.
        Args:
          secret_without_spaces (str):
            User secret which is used in generating one
            time password.
        """

        return secret_without_spaces.upper()

    def decode_with_base32(self, upper_case_secret):
        """Returns a value whihc decoded by Base32.
        Args:
          upper_case_secret (str):
            User secret which is used in generating one
            time password.
        """

        return base64.b32decode(upper_case_secret)

    def current_timestamp(self):
        """Returns the current UNIX time.
        """
        return time.time()

    def create_hmac(self, secret, input):
        """Returns the hash value which is used in
        creating one time password.
        Args:
          secret (str):
            User secret which is used in generating one
            time password.
          input (float):
            The value of current UNIX time divided by 30.
        """

        input_str = repr(input).encode('ascii')
        input_hash = hashlib.sha1(secret + input_str).hexdigest().encode('ascii')
        return hashlib.sha1(secret + input_hash).hexdigest()

    def one_time_password(self):
        """Create the one time password using secret
        which must be set in constructor.
        """
        secret_without_spaces = self.remove_spaces(self._secret)
        upper_case_secret = self.to_upper_case(secret_without_spaces)
        secret = self.decode_with_base32(upper_case_secret)
        input = self.current_timestamp() / 30
        hmac = self.create_hmac(secret, input)
        offset = ord(hmac[len(hmac)-1]) & 0x0F
        hex_four_characters = binascii.hexlify(hmac[offset : offset+4].encode())
        password = int(hex_four_characters, 32) % 1000000
        return password
