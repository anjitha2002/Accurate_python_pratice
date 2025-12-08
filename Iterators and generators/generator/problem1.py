def readfiles(file1):
    for f in file1:

        file=open(f,'r')
        for line in file:
            yield line

def grep(pattern,lines):
    return(line for line in lines if pattern in line)


def printlines(lines):
    for line in lines:
        print(line,end="")

def main(pattern,file1):
    lines=readfiles(file1)
    lines=grep(pattern,lines)
    printlines(lines)

print(main('simple',['file1']))


