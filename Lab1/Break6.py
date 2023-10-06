import time
import subprocess
import hashlib
   
start = time.time()
passwords=[i.strip() for i in open('PwnedPWs100k')]
gang=[i.strip() for i in open('gang')]
saltedpasswords = [i.strip() for i in open('SaltedPWs')]


salt = dict()
for i in saltedpasswords:
    if i.split(',')[0] in gang:
        salt[i.split(',')[1]] = i.split(',')[0] + i.split(',')[2]


new_passwords = dict()
for i in passwords:
    for j in range(100):
        new_passwords[i + str(j)] = hashlib.sha256(bytes(i + str(j) + salt[i.split(',')[1]], 'utf-8')).hexdigest()


matched = []
for name in salt:
    for pw in new_passwords:
        if salt[name] == new_passwords[pw]:
            matched.append((name, pw))


password = []
for name in new_passwords:
    for found in matched:
        if name == found[1]:
            password.append((found[0], name))


for name in salt:
    for p in password:
        if name == p[0]:
            command = subprocess.run(["python3", "Login.pyc", name, p[1]], capture_output = True, text=True)
            if "success" in command.stdout:
                print("Cracked username " + name)
                print("Cracked password " + p[1])


end = time.time() - start
print(str(end) + " seconds")
