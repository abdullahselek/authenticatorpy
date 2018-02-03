#!/usr/bin/env python

import base64
import time
import hashlib
import binascii

class Authenticator(object):
    """Authenticator class which generates unique one
    time use password.
    """

    def __init__(self, secret=None):
        """Returns a Authenticator instance.
        Args:
          secret (str):
            User secret which is used in generating one
            time password.
        """

        self._secret = secret

    def remove_spaces(self, secret):
        """Returns a new string including no space.
        Args:
          secret (str):
            User secret which is used in generating one
            time password.
        """

        secret_without_spaces = secret.replace(' ', '')
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
