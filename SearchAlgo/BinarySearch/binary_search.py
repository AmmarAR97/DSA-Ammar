"""
1. When I try to find number 5 in below list using binary search, it doesn't work and returns me -1 index. Why is that?

    numbers = [1,4,6,9,10,5,7]

---> Because the list is not sorted.

    
2. Find index of all the occurances of a number from sorted list

    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15  

   This should return 5,6,7 as indices containing number 15 in the array
"""


def binary_search(num_list, target_num):

    left = 0
    right = len(num_list) - 1
    
    while left <= right:

        mid = (left + right) // 2

        if num_list[mid] == target_num:
            return mid
        elif num_list[mid] < target_num:
            left = mid + 1
        else:
            right = mid - 1
    else:
        return -1


def binary_search_many(num_list, target_num):

    left = 0
    right = len(num_list) - 1

    op = []
    
    while left <= right:

        mid = (left + right) // 2

        if num_list[mid] == target_num:
            op.append(mid)
            print(op)
        
        if num_list[mid] < target_num:
            left = mid + 1
        else:
            right = mid - 1

    return op



if __name__ == "__main__":

    num_list = [1,4,6,9,11,15,15,15,15,17,21,34,34,56]
    target = 15

    # print("Result:, ", binary_search(num_list, target))


    print("Result:", binary_search_many(num_list, target))
