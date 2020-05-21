import time
import os
import paramiko
from getpass import getpass, getuser

HOST = os.getenv('HOST')
USER = os.getenv('USER')
PWD = os.getenv('PASSWORD')

client = paramiko.SSHClient()

if __name__ == '__main__':
    try:
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

        if HOST is None:
            HOST = input('write host to connect: ')

        if USER is None:
            USER = input('write user: ')

        if PWD is None:
            PWD = getpass('write your password: ')

        client.connect(HOST, username=USER, password=PWD)

        stdin, stdout, stderr = client.exec_command('ls')

        time.sleep(1)

        result = stdout.read().decode()
        print(result, end='\n')
    except paramiko.ssh_exception.AuthenticationException:
        print('Authentication fail', end='\n')
    except paramiko.ssh_exception.SSHException as e:
        print(e, end='\n')
    except KeyboardInterrupt:
        print('Program finished', end='\n')
    except TimeoutError:
        print('Timeout connection', end='\n')
    finally:
        client.close()
