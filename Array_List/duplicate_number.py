# Duplicate Numbers
def remove_duplicates(lst):
    # Soln: 1
    # unique_lst = []
    # seen = set()
    # for item in lst:
    #     if item not in seen:
    #         unique_lst.append(item)
    #         seen.add(item)
    # return unique_lst

    # Soln: 2
    # return list(set(arr))

    # Soln: 3
    unique_lst = []
    
    for num in arr:
        if num not in unique_lst:
            unique_lst.append(num)
            
    return unique_lst

my_list = [1, 1, 2, 2, 3, 4, 5]
print(remove_duplicates(my_list))  # Output: [1, 2, 3, 4, 5]