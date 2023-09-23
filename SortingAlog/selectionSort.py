"""
divide array into sorted and unsorted
find the min value and swap it with 0th index in the first iteration
repeat from i+1 index
"""

def selectionSort(unsortedList):
	for i in range(len(unsortedList)):
		min_index = i
		for j in range(i+1, len(unsortedList)):
			if unsortedList[min_index] > unsortedList[j]:
				min_index = j
		unsortedList[i], unsortedList[min_index] = unsortedList[min_index], unsortedList[i]

	return unsortedList

print(selectionSort([5,2,6,12,1,8,3,9]))