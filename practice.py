# Find the Maximum and Minimum Elements in a List
# Write a Python function to find the maximum and minimum elements in a given list.
from importlib.resources.readers import remove_duplicates

list = [3, 1, 4, 1, 5, 9]
def find_max_min(lst):
    maximum = minimum = lst[0]
    for num in lst[1:]:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    return maximum, minimum
print(find_max_min(list))


# Remove Duplicates from a List
# Write a Python function to remove duplicates from a list while preserving the order.
list = [1, 2, 2, 3, 4, 4, 5]

def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result


print(remove_duplicates(list))



# Find the Intersection of Two Lists
# Write a Python function to find the intersection of two lists.

def intersection(list1, list2):
    result = []
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(intersection(list1, list2))
