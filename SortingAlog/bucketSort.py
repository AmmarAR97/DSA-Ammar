import math

def insertionSort(unsortedList):
	for i in range(1, len(unsortedList)):
		key = unsortedList[i]
		j = i - 1
		while j >= 0 and key < unsortedList[j]:
			unsortedList[j+1] = unsortedList[j]
			j -= 1
		unsortedList[j+1] = key
	return unsortedList


def bucketSort(unsortedList):
	
	# Find the number of buckets to be created
	total_buckets = round(math.sqrt(len(unsortedList)))

	# Find the maximum element of the list
	max_element = max(unsortedList)

	# Create empty buckets
	buckets = [ [] for _ in range(total_buckets) ]

	# Add elements to the respective buckets
	for num in unsortedList:

		# from the below formula we find out index of the bucket where this element is to be inserted
		bucket_index = math.ceil(num*(total_buckets/max_element))

		# Append the element to the respective bucket
		buckets[bucket_index-1].append(num)

	# Sort all the buckets individually
	for i in range(len(buckets)):
		buckets[i] = insertionSort(buckets[i])

	# Merger them into a single array
	k = 0
	for i in range(len(buckets)):
		for j in range(len(buckets[i])):
			unsortedList[k] = buckets[i][j]
			k += 1

	return unsortedList

print(bucketSort([12,11,10,9,8,7,6,5,4,3,2,1]))