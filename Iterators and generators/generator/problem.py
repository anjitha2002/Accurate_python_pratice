def cat(file1):
    for f in file1:
        file=open(f,'r')
        for line in file:
            print(line, end="")
print(cat(["file1"]))


def grep(pattern, file1):
    for f in file1:
        with open(f,'r') as file:
            for line in file:

                if pattern in line:
                    print(line, end="")
print(grep('a', ['file1']))



