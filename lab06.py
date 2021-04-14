from Apartment import Apartment

def mergesort(apartmentList):
	if len(apartmentList) > 1:
		mid = len(apartmentList) // 2
		left = apartmentList[:mid]
		right = apartmentList[mid:]

		mergesort(left)
		mergesort(right)
		i, j, k = 0, 0, 0 

		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				apartmentList[k] = left[i]
				i += 1
			else:
				apartmentList[k] = right[j]
				j += 1
			k += 1

		while i < len(left):
			apartmentList[k] = left[i]
			i += 1
			k += 1

		while j < len(right):
			apartmentList[k] = right[j]
			j += 1
			k += 1

def ensureSortedAscending(apartmentList):
	i = 0
	if len(apartmentList) <= 1:
		return True

	while i < len(apartmentList)-1:
		if (apartmentList[i] < apartmentList[i+1]) or (apartmentList[i] == apartmentList[i+1]):
			i += 1
		else:
			return False
	return True

def getNthApartment(apartmentList, n):
	n = n-1
	if n in range(0, len(apartmentList)):
		return str(apartmentList[n].getApartmentDetails())
	else:
		return "(Apartment {}) DNE".format(n+1)

def getTopThreeApartments(sorted_apartmentList):
	if len(sorted_apartmentList) == 0 or len(sorted_apartmentList) == 1:
		return sorted_apartmentList
	if len(sorted_apartmentList) == 2:
		return "1st: {}, 2nd: {}".format(sorted_apartmentList[0].getApartmentDetails(), sorted_apartmentList[1].getApartmentDetails())
	else:
		return "1st: {}, 2nd: {}, 3rd: {}".format(sorted_apartmentList[0].getApartmentDetails(), sorted_apartmentList[1].getApartmentDetails(), sorted_apartmentList[2].getApartmentDetails())