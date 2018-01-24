#!/usr/bin/env python

import base64
import time

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

    def encode_with_base32(self, upper_case_secret):
        return base64.b32encode(self.byte_array(upper_case_secret))

    def current_timestamp(self):
        return time.time()
