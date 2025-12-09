
# Problem 5: Write a function tree_reverse to reverse elements of a nested-list recursively.
def tree_reverse(list):
    rev_list=[]
    for l in list[::-1] :
        if type(l)==list:
            rev_list.append(tree_reverse(l))
        else:
            rev_list.append(l)

    return rev_list
print(tree_reverse([1, [2, 3], [4, [5, 6]]]))
