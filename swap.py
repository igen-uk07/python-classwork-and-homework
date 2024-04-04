#without function

lst = [1, 2, 3, 4, 5]
print("Original list:", lst)
if len(lst) < 2:
        print("The list must have at least two elements.")
else:
    lst[0], lst[-1] = lst[-1], lst[0]
    print("List after swapping first and last elements:", lst)


#with function
def swap(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

list = [10,20,30]
print("Original List:", list)
swapped_list = swap(list)
print("After swapping:", swapped_list)