
# Problem 5: Write a function to compute the total number of lines of code in all python files in the specified directory recursively.
import os
def count_lines(path):
    total_lines=0
    for entry in os.listdir(path):
        full_path=os.path.join(path,entry)
        if os.path.isfile(full_path) and full_path.endswith(".py"):
            file=open(full_path,'r')
            total_lines +=len(file.readlines())
        else:
            total_lines +=count_lines(full_path)
    return total_lines
print(count_lines(r"C:/Users/ASUS/PycharmProjects/Accurate pratice/Iterators and generators"))