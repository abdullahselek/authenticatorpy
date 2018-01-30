#!/usr/bin/env python

import base64
import time
import hashlib
import binascii

class Authenticator(object):

    def __init__(self, secret=None):
        self._secret = secret

    def remove_spaces(self, secret):
        secret_without_spaces = secret.replace(' ', '')
        return secret_without_spaces

    def to_upper_case(self, secret_without_spaces):
        return secret_without_spaces.upper()

    def byte_array(self, str):
        byte_array = bytearray()
        byte_array.extend(map(ord, str))
        return byte_array

    def decode_with_base32(self, upper_case_secret):
        return base64.b32decode(upper_case_secret)

    def current_timestamp(self):
        return time.time()

    def create_hmac(self, secret, input):
        input_str = repr(input).encode('ascii')
        input_hash = hashlib.sha1(secret + input_str).hexdigest().encode('ascii')
        return hashlib.sha1(secret + input_hash).hexdigest()

    def get_last_x_bytes(self, byte_array, x):
        return byte_array[-x:]

    def one_time_password(self):
        secret_without_spaces = self.remove_spaces(self._secret)
        upper_case_secret = self.to_upper_case(secret_without_spaces)
        secret = self.decode_with_base32(upper_case_secret)
        input = self.current_timestamp() / 30
        hmac = self.create_hmac(secret, input)
        item = ord(hmac[len(hmac)-1])
        offset = (item & 0x0F) >> 4
        hex_four_characters = binascii.hexlify(hmac[offset : offset+4].encode())
        password = int(hex_four_characters, 16) % 1000000
        return password
