"""
compare 0 and 1 index and swap based on icreasing or decreasing sort.
follow up with 1 and 2
"""

def bubbleSort(unsortedList):
	for i in range(0, len(unsortedList)):
		for j in range(len(unsortedList)-i-1):
			if unsortedList[j] > unsortedList[j+1]:
				unsortedList[j], unsortedList[j+1]= unsortedList[j+1], unsortedList[j]

	return unsortedList

print(bubbleSort([5,2,6,12,1,8,3,9]))
