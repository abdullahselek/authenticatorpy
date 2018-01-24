#!/usr/bin/env python

class Authenticator(object):

    def __init__(self,
                 secret=None):
        self._secret = secret
