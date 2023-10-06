import time
import subprocess
import hashlib




start = time.time()
passwords=[i.strip() for i in open('PwnedPWs100k')]
gang=[i.strip() for i in open('gang')]
hashed_passwords = [i.strip() for i in open('HashedPWs')]




hashed = {}
for i in hashed_passwords:
    if i.split(',')[0] in gang:
        hashed[i.split(',')[0]] = i.split(',')[1]


new_password = {}
for i in passwords:
    for j in range(100):
        new_password[i + str(j)] = hashlib.sha256(bytes(i + str(j), 'utf-8')).hexdigest()


found = []
for name, hashed_password in hashed.items():
  for password, f in new_password.items():
    if hashed_password == f:
      found.append((name, password))
   
original = []
for password in new_password.keys():
  for match in found:
    if password == match[1]:
      original.append((match[0], password))




for name in hashed.keys():
  for og in original:
    if name == og[0]:
      command = subprocess.run(["python3", "Login.pyc", name, og[1]], capture_output = True, text=True)
      if "success" in command.stdout:
        print("Cracked username " + name)
        print("Cracked password " + og[1])
                   
end = time.time() - start
print(str(end) + " seconds")
