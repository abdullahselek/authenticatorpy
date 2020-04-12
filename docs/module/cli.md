# CLI

CLI helps you to simulate creating tokens with your secret keys and optional time to live values.

## Usage

First you need to install **authenticatorpy** either from PyPi or source. Then you can use sample
commands below.

This will create you new tokens with 30 seconds gaps.

```console
$ python -m authenticatorpy --secret testsecret
```

With this one you can set your own time gaps, as an example 5 seconds.

```console
$ python -m authenticatorpy --secret testsecret --time 5
```
