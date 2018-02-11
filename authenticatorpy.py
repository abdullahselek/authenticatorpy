#!/usr/bin/env python

import sys
import argparse
import sched
import time

from authenticatorpy.authenticator import Authenticator

def create_one_time_password(scheduler, authenticator):
    scheduler.enter(30, 0, create_one_time_password, (scheduler, authenticator))
    print(authenticator.one_time_password())


if __name__ == '__main__':

    print('Started each 30 seconds a new token will be created')

    parser = argparse.ArgumentParser(description='Authenticator 2FA token generator')
    parser.add_argument('--secret', type=str, help='secret string for user')
    args = parser.parse_args()

    if len(sys.argv) < 2:
        print('Specify a secret key to use')
        sys.exit(1)

    # Optional bash tab completion support
    try:
        import argcomplete
        argcomplete.autocomplete(parser)
    except ImportError:
        pass

    secret = sys.argv[2]
    authenticator = Authenticator(secret)

    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(0, 0, create_one_time_password, (scheduler, authenticator))
    scheduler.run()
