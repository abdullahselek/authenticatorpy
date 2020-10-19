#!/usr/bin/env python

import sys
import argparse
import sched
import time

from authenticatorpy.authenticator import Authenticator


def create_one_time_password(scheduler, authenticator, sleep_time):
    scheduler.enter(
        sleep_time, 0, create_one_time_password, (scheduler, authenticator, sleep_time)
    )
    print(authenticator.one_time_password(sleep_time))


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Authenticator 2FA token generator")
    parser.add_argument("--secret", type=str, help="secret string for user")
    parser.add_argument(
        "--time",
        type=int,
        help="optional delay to generate another new token (default 30 seconds)",
    )
    args = parser.parse_args()

    if len(sys.argv) < 2:
        print("Specify a secret key to use")
        sys.exit(1)

    # Optional bash tab completion support
    try:
        import argcomplete

        argcomplete.autocomplete(parser)
    except ImportError:
        pass

    secret = sys.argv[2]
    authenticator = Authenticator(secret)

    sleep_time = 30
    if len(sys.argv) > 4:
        sleep_time = float(sys.argv[4])

    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(
        0, 0, create_one_time_password, (scheduler, authenticator, sleep_time)
    )
    scheduler.run()
