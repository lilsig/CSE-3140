import hashlib
import os
def match(filename):
    path = '/home/cse/Lab3/Q2files'
    os.chdir(path)
    with open(filename,"rb") as f:
        byte = f.read()
        hashed = hashlib.sha256(byte).hexdigest()
        if hashed == "5220fd45327e9e5c3332b9aadbdd51a5268f3f1351d257281499bbb11ca433ca":
            return True
        return False
if __name__ == "__main__":
    ans = []
    path = '/home/cse/Lab3/'
    os.chdir(path)
    for filename in os.listdir('Q2files'):
        if match(filename):
            ans.append(filename)
    print(ans)
