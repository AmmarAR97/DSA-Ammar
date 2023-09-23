# Best Score
def first_second(my_list):

    # Soln: 1

    # max1, max2 = float('-inf'), float('-inf')

    # for num in my_list:
    #     if num > max1:
    #         max2 = max1
    #         max1 = num
    #     elif num > max2 and num != max1:
    #         max2 = num

    # return max1, max2

    # Soln: 2
    # my_list.sort()
    # return my_list[-1], my_list[-2]

    # Soln: 3
    first_best, second_best = -1, -1
    for num in my_list:
        if num > first_best:
            second_best = first_best
            first_best = num
    return first_best, second_best

my_list = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(first_second(my_list))  # Output: (90, 87)