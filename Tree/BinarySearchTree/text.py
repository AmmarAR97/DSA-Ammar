array = [1,2,3,4,5]
# # b = array
# # c = shallo copy
# # d = deepcopy 
# array.reverse()
# print(array)
# print(array[::-1])

# # It should be sorted

# def binary_search(array, target_num):	

# 	left = 0
# 	right = len(array) - 1

# 	while left < right:

# 		mid = (left + right) // 2

# 		if array[mid] == target_num:
# 			return "Found target"
# 		elif target_num > array[mid]:
# 			left = mid+1
# 		else:
# 			right = mid - 1

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


print(binary_search(array, 2))

# array[1] = "ammar"
# print(array)
# tuple(array)
# array[1] = 1
# print(array)

# array = [1,2,3,4,5]  

# class MyClass:

# 	def __init__(self, obj1, obj2):
# 		self.obj1 = obj1
# 		self.obj2 = obj2

# 	def my_func(self):
# 		my_func_var = "A"
# 		return my_func_var


