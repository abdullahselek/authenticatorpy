#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from authenticatorpy.authenticator import Authenticator


class AuthenticatorTest(unittest.TestCase):
    def setUp(self):
        self._authenticator = Authenticator("abcd xyzw abcd xyzw abcd xyzw abcd xyzw")

    def test_initiation(self):
        self.assertIsInstance(self._authenticator, Authenticator)

    def test_wrong_initiation(self):
        with self.assertRaises(Exception) as context:
            Authenticator(123456)

        self.assertTrue(
            "You must set a str variable as secret!" in str(context.exception)
        )

        with self.assertRaises(Exception) as context:
            Authenticator("abcd")

        self.assertTrue(
            "You must set a secret of minimum 8 characters!" in str(context.exception)
        )

        with self.assertRaises(Exception) as context:
            Authenticator("ĀƯŤĤËŊŦĩÇÁƮŏƦ")

        self.assertTrue(
            "You must set an ascii str variable as secret!" in str(context.exception)
        )

        with self.assertRaises(Exception) as context:
            Authenticator(lambda: None)

        self.assertTrue(
            "You must set a str variable as secret!" in str(context.exception)
        )

        with self.assertRaises(Exception) as context:
            Authenticator(123456.789)

        self.assertTrue(
            "You must set a str variable as secret!" in str(context.exception)
        )

        with self.assertRaises(Exception) as context:
            Authenticator([])

        self.assertTrue(
            "You must set a str variable as secret!" in str(context.exception)
        )

        with self.assertRaises(Exception) as context:
            Authenticator(set())

        self.assertTrue(
            "You must set a str variable as secret!" in str(context.exception)
        )

        with self.assertRaises(Exception) as context:
            Authenticator(tuple())

        self.assertTrue(
            "You must set a str variable as secret!" in str(context.exception)
        )

        with self.assertRaises(Exception) as context:
            Authenticator("abcd efg0")

        self.assertTrue(
            "All characters in the secret must be alphabetic!" in str(context.exception)
        )

    def test_remove_spaces(self):
        string_without_spaces = self._authenticator.remove_spaces(
            "abcd xyzw abcd xyzw abcd xyzw abcd xyzw"
        )
        self.assertEqual(string_without_spaces, "abcdxyzwabcdxyzwabcdxyzwabcdxyzw")
        string_without_spaces = self._authenticator.remove_spaces(
            "abcd \tyzw \nbcd \tyzw"
        )
        self.assertEqual(string_without_spaces, "abcdyzwbcdyzw")

    def test_to_upper_case(self):
        upper_case_str = self._authenticator.to_upper_case("abcdefgh")
        self.assertEqual(upper_case_str, "ABCDEFGH")
        upper_case_str = self._authenticator.to_upper_case("aBcDeFgH")
        self.assertEqual(upper_case_str, "ABCDEFGH")

    def test_decode_with_base32(self):
        decoded_str = self._authenticator.decode_with_base32(
            "ABCDXYZWABCDXYZWABCDXYZWABCDXYZW"
        )
        self.assertEqual(decoded_str, b"\x00D;\xe36\x00D;\xe36\x00D;\xe36\x00D;\xe36")

    def test_current_timestamp(self):
        self.assertIsNotNone(self._authenticator.current_timestamp())

    def test_create_hmac(self):
        decoded_str = self._authenticator.decode_with_base32(
            "ABCDXYZWABCDXYZWABCDXYZWABCDXYZW"
        )
        input = self._authenticator.current_timestamp() / 30
        hmac = self._authenticator.create_hmac(decoded_str, input)
        self.assertIsNotNone(hmac)

    def test_one_time_password(self):
        password = self._authenticator.one_time_password()
        self.assertIsNotNone(password)
        self.assertIsNotNone(Authenticator("abcd xyzw a").one_time_password())
        self.assertIsNotNone(Authenticator("abcd xyzw ab").one_time_password())
        self.assertIsNotNone(Authenticator("abcd xyzw abcd").one_time_password())

    def test_one_time_password_with_empty_spaces(self):
        password = Authenticator("\ta\bt\tc\td \te\tf\tg\th").one_time_password()
        self.assertIsNotNone(password)
        password = Authenticator("\ra\rb\rc\rd \re\rf\rg\rh").one_time_password()
        self.assertIsNotNone(password)
