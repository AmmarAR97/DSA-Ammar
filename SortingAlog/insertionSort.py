# Define a function named insertionSort that takes an unsorted list as input.
def insertionSort(unsortedList):
	# Iterate through the list starting from the second element (index 1).
	for i in range(1, len(unsortedList)):
		# Store the current element in the 'key' variable.
		key = unsortedList[i]
		# Initialize 'j' to the index before the current element.
		j = i - 1
		# Compare 'key' with elements before it and shift them right until
		# the correct position for 'key' is found.
		while j >= 0 and key < unsortedList[j]:
			unsortedList[j+1] = unsortedList[j]  # Shift the element to the right.
			j -= 1  # Move to the previous element.
		# Place 'key' in its correct position in the sorted portion of the list.
		unsortedList[j+1] = key
	# Return the sorted list.
	return unsortedList

# Call the insertionSort function with an unsorted list as an argument and print the result.
print(insertionSort([5, 2, 6, 12, 1, 8, 3, 9]))
