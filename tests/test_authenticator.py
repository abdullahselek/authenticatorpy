#!/usr/bin/env python

import unittest
from authenticatorpy.authenticator import Authenticator

class AuthenticatorTest(unittest.TestCase):

    def setUp(self):
        self._authenticator = Authenticator('abcd 1234 abcd 1234 abcd 1234 abcd 1234')

    def test_initiation(self):
        self.assertIsInstance(self._authenticator, Authenticator)
    
    def test_remove_spaces(self):
        string_without_spaces = self._authenticator.remove_spaces('abcd 1234 abcd 1234 abcd 1234 abcd 1234')
        self.assertEqual(string_without_spaces, 'abcd1234abcd1234abcd1234abcd1234')
    
    def test_to_upper_case(self):
        upper_case_str = self._authenticator.to_upper_case('abcd')
        self.assertEqual(upper_case_str, 'ABCD')
        upper_case_str = self._authenticator.to_upper_case('aBcD')
        self.assertEqual(upper_case_str, 'ABCD')

    def test_encode_with_base32(self):
        decoded_str = self._authenticator.encode_with_base32('ABCD1234ABCD1234ABCD1234ABCD1234')
        self.assertEqual(decoded_str, b'IFBEGRBRGIZTIQKCINCDCMRTGRAUEQ2EGEZDGNCBIJBUIMJSGM2A====')

    def test_current_timestamp(self):
        self.assertIsNotNone(self._authenticator.current_timestamp())
