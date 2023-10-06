import os


if __name__ == "__main__":


    directory = os.listdir(path=".")
   
    print("Found python files:")
   
    pythonFiles = []
    for f in directory:
        if ".py" in f:
            pythonFiles.append(f)
            print(f)