#!/usr/bin/env python

import unittest
from authenticatorpy.authenticator import Authenticator

class AuthenticatorTest(unittest.TestCase):

    def setUp(self):
        self._authenticator = Authenticator('1234 1234 1234 1234 1234 1234 1234 1234')

    def test_initiation(self):
        self.assertIsInstance(self._authenticator, Authenticator)
