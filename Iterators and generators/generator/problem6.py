
# Problem 6: Write a function to compute the total number of lines of code, ignoring empty and comment lines, in all python files in the specified directory recursively.
import os
def count_lines(path):
    count=0
    for i in os.listdir(path):
        full_path=os.path.join(path,i)
        if os.path.isfile(full_path) and full_path.endswith(".py"):
            file=open(full_path,'r')
            for line in file:
                line=line.strip()
                if line!="" and not line.startswith("#"):
                    count +=1
                elif os.path.isdir(full_path):
                    count +=count_lines(full_path)
    return count
print(count_lines(r"C:/Users/ASUS/PycharmProjects/Accurate pratice/Iterators and generators"))
            