# Problem 2: Write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters.
def readfiles(files):
    for f in files:
        file=open(f,'r')
        for line in file:
            yield line
def long_line(lines,n=40):
    return(line for line in lines if len(line)>n)

def printlines(lines):
    for line in lines:
        print(line,end="")

def main(filelist):
    lines=readfiles(filelist)
    long=long_line(lines)
    printlines(long)
print(main(['file1','file2']))