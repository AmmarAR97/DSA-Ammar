def insertionSort(unsortedList):
	for i in range(1, len(unsortedList)):
		key = unsortedList[i]
		j = i - 1
		while j >= 0 and key < unsortedList[j]:
			unsortedList[j+1] = unsortedList[j]
			j -= 1
			print(unsortedList)
		unsortedList[j+1] = key
		print("s",unsortedList)
	return unsortedList

print(insertionSort([5,2,6,12,1,8,3,9]))