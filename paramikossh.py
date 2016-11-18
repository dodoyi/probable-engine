import paramiko
hostname = '192.168.18.183'
username = 'root'
passwd = '123456'
port = 22

if __name__=='__main__':
    # paramiko.util.log_to_file('paramiko.log')
    s=paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname = hostname,username = username ,password=passwd)
    stdin,stdout,stderr=s.exec_command('hostname'
                                       ';echo hello'
                                       ';uname -a')
    print (stdout.read())
    s.close()


