#!/usr/bin/env python

import sys
import base64
import time
import hashlib
import binascii
import re


class Authenticator(object):
    """Authenticator class which generates unique one time use password."""

    def __init__(self, secret: str):
        """Creates a new Authenticator instance.
        Args:
          secret (str):
            User secret which is used in generating one
            time password.
        Returns:
          Authenticator instance.
        """

        self._secret = secret
        self.__check_secret(secret)

    def __is_ascii(self, secret: str):
        return all(ord(c) < 128 for c in secret)

    def __is_alpha(self, secret: str):
        return all(c.isalpha() for c in secret)

    def __check_secret(self, secret: str):
        if isinstance(secret, str) == False:
            raise TypeError("You must set a str variable as secret!")
        if self.__is_ascii(secret) == False:
            raise TypeError("You must set an ascii str variable as secret!")
        secret_without_spaces = self.remove_spaces(secret)
        self._secret = self.to_upper_case(secret_without_spaces)
        secret_length = len(self._secret)
        if secret_length < 8:
            raise ValueError("You must set a secret of minimum 8 characters!")
        if secret_length > 8:
            index = secret_length % 8
            self._secret = self._secret[:-index]
        if self.__is_alpha(self._secret) == False:
            raise TypeError("All characters in the secret must be alphabetic!")

    def remove_spaces(self, secret: str) -> str:
        """Removes empty spaces from given string.
        Args:
          secret (str):
            User secret which is used in generating one
            time password.
        Returns:
          String without empty spaces.
        """

        secret_without_spaces = secret.replace(" ", "")
        secret_without_spaces = re.sub(r"\W", "", secret_without_spaces)
        return secret_without_spaces

    def to_upper_case(self, secret_without_spaces: str) -> str:
        """Updates given string to uppercase without changing.
        Args:
          secret_without_spaces (str):
            User secret which is used in generating one
            time password.
        Returns:
          String in uppercase.
        """

        return secret_without_spaces.upper()

    def decode_with_base32(self, upper_case_secret: str) -> bytes:
        """Creates a new Base32 decoded value from given string.
        Args:
          upper_case_secret (str):
            User secret which is used in generating one
            time password.
        Returns:
          Base32 decoded value.
        """

        return base64.b32decode(upper_case_secret)

    def current_timestamp(self) -> time:
        """Returns the current UNIX time."""

        return time.time()

    def create_hmac(self, secret: str, input: float) -> str:
        """Creates the hash value which is used in creating one time password.
        Args:
          secret (str):
            User secret which is used in generating one
            time password.
          input (float):
            The value of current UNIX time divided by 30.
        Returns:
          SHA1 hash value.
        """

        input_str = repr(input).encode("ascii")
        input_hash = hashlib.sha1(secret + input_str).hexdigest().encode("ascii")
        return hashlib.sha1(secret + input_hash).hexdigest()

    def one_time_password(self, delay_time: float = 30.0) -> str:
        """Creates one time password using secret which must be set in constructor.
        Args:
          delay_time (float):
            Optional time interval for token availability.
        Returns:
          One time password as string.
        """

        secret_without_spaces = self.remove_spaces(self._secret)
        upper_case_secret = self.to_upper_case(secret_without_spaces)
        secret = self.decode_with_base32(upper_case_secret)
        input = self.current_timestamp() / delay_time
        hmac = self.create_hmac(secret, input)
        offset = ord(hmac[len(hmac) - 1]) & 0x0F
        hex_four_characters = binascii.hexlify(hmac[offset : offset + 4].encode())
        password = int(hex_four_characters, 32) % 1000000
        return password
