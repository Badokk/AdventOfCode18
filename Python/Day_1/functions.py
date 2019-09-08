
def sum_list(number_list):
	sum = 0
	for number in number_list:
		sum = sum + int(number)
	return sum
	
	
def find_first_partial_sum_duplicate(number_list):
	# # Brute force approach. Not very elegant
	# previouslyFoundNumbers = set()
	# sum = 0
	# while True:
	# 	for number in number_list:
	# 		sum = sum + int(number)
	# 		# print(str(len(previouslyFoundNumbers)) + " " + str(sum))
	# 		if (sum in previouslyFoundNumbers):
	# 			return sum
	# 		previouslyFoundNumbers.add(sum)

	return (False, None)
			