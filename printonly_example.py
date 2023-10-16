import itertools
import time
import string

host = "127.0.0.1"
username = "root"

## Brute Force Example


def brute_force():
    alphanumeric = string.ascii_letters + string.digits
    for password in itertools.product(alphanumeric, repeat=6):
        yield ''.join(password)


for password in brute_force():
    print(f'trying: {password}')


## Dictionary Example

with open('/passwords.txt', 'r') as f:
    passwords = f.read().splitlines()
    for password in passwords:
        print(f'trying: {password}')
