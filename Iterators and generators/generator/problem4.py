# Problem 4: Write a function to compute the number of python files (.py extension) in a specified directory recursively.
import os
def count_files(path):
    count=0
    for entry in os.listdir(path):
        full_path=os.path.join(path,entry)
        if os.path.isfile(full_path):
            if full_path.endswith(".py"):
                count +=1
        else:
            count +=count_files(full_path)
    return count
print(count_files(r"C:/Users/ASUS/PycharmProjects/Accurate pratice/Iterators and generators" ))