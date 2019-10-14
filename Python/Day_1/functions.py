
def sum_list(number_list):
	sum = 0
	for number in number_list:
		sum = sum + int(number)
	return sum
	
def prepare_partial_sums(number_list):
	initial_partial_sums = list()
	partial_sum = 0
	for number in number_list:
		initial_partial_sums.append(partial_sum)
		partial_sum += int(number)
	
	total = partial_sum
	return initial_partial_sums, total

def prepare_congruent_groups(partial_sums, total):
	grouped_partial_sums = dict()
	for number in partial_sums:
		remainder = number % total if total != 0 else number
		if not remainder in grouped_partial_sums:
			grouped_partial_sums[remainder] = list()
		
		grouped_partial_sums[remainder].append(number)
	return grouped_partial_sums

def find_candidates(grouped_partial_sums):
	candidate_pairs = dict()
	smallest_step = -1 # would be nice to get the first pair straight away
	for key in grouped_partial_sums:
		grouped_partial_sums[key].sort()
		last_value = -1 # same
		for value in grouped_partial_sums[key]:
			if (last_value == -1):
				last_value = value
				continue
			step = value - last_value
			if (smallest_step == -1):
				smallest_step = step
			if (step < smallest_step):
				candidate_pairs.clear()
			if (step == smallest_step):
				if not key in candidate_pairs:
					candidate_pairs[key] = list()
				candidate_pairs[key].append({last_value, value})
			last_value = value
	return candidate_pairs
			# weird, it seems to be working. well, let's add more tests just in case

			



	
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
	
	### Prepare partial sums
	(initial_partial_sums, total) = prepare_partial_sums(number_list)

	# if total == 0:
	# 	special case, need to sort the partial sums and check for duplicates
	# 	return

	### Prepare congruent groups
	grouped_partial_sums = prepare_congruent_groups(initial_partial_sums, total)

	# now the groups would likely need to be checked for duplicates... Or should
	# they? the generic behaviour should point out duplicates quite easily
	print(grouped_partial_sums)
	for key in grouped_partial_sums:
		print(key, grouped_partial_sums[key])

	indices_to_delete = list()
	for key in grouped_partial_sums: # i wonder if there's a kind of foreach that'd fit here
		if (len(grouped_partial_sums[key]) < 2):
			indices_to_delete.append(key)

	for key in indices_to_delete:
		del grouped_partial_sums[key]

	print(grouped_partial_sums)
	for key in grouped_partial_sums:
		print(key, grouped_partial_sums[key])

	# good. Now, there are two ways:
	# 1. There are groups with more than one member -> find candidates fot title of first dupe
	# 2. There are no such groups return false.

	# candidates = findCandidates(groupedPartialSums)
	

	return (False, None)
			