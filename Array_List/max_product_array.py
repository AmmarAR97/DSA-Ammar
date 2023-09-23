# Find max product of two integer

# Soln 1:

# def max_product(arr):
#     arr.sort(reverse=True)
#     return arr[0]*arr[1]

# Soln 2:
# def max_product(arr):
#     # Initialize two variables to store the two largest numbers
#     max1, max2 = 0, 0  # O(1), constant time initialization

#     # Iterate through the array
#     for num in arr:  # O(n), where n is the length of the array
#         # If the current number is greater than max1, update max1 and max2
#         if num > max1:  # O(1), constant time comparison
#             max2 = max1  # O(1), constant time assignment
#             max1 = num  # O(1), constant time assignment
#         # If the current number is greater than max2 but not max1, update max2
#         elif num > max2:  # O(1), constant time comparison
#             max2 = num  # O(1), constant time assignment

#     # Return the product of the two largest numbers
#     return max1 * max2  # O(1), constant time multiplication

# Soln 3:
def max_product(arr):
    max_prod = 0
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            prod = arr[i] * arr[j]
            if prod > max_prod:
                max_prod = prod
    return max_prod

arr = [1, 7, 3, 4, 9, 5]
print(max_product(arr))  # Output: 63 (9*7)