
# Problem 7: Write a program split.py, that takes an integer n and a filename as command line arguments and splits the file into multiple small files with each having n lines.

import sys
n = int(sys.argv[1])
file2 = sys.argv[2]

f= open(file2,'r')
line=f.readlines()
f.close()
part=1
i=0
while i<len(line):
    part_lines=open(f"{file2}_part{part}.txt","w")
    part_lines.writelines(line[i:i+n])
    part_lines.close()
    part+=1
    i+=n


