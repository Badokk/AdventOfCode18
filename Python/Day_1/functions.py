import math
##### Part 1 #####


def sum_list(number_list):
    sum = 0
    for number in number_list:
        sum = sum + int(number)
    return sum

##### Part 2 #####

# Finally, done. Oh, boy. This looks way messier than I've imagined... And I really don't feel like cleaning it up now.
# So, if I ever happen to get back to this:
# 1. Sanity checks! Most functions here work only if input makes sense
# 2. Optional output. Putting real values in clutters the console.
# 3. This is more for future reference - need something akin to headers,
#	 so that I could put the main method at the top instead of bottom.
#
# What are the complexities of main and brute force solutions? Was it worth it to pump out this much code for such simple a thing?
# Let's see... BF is potentially an infinite loop, so congruent groups or total==0 sanity check would be a must. So, assuming the input has a solution,
# we're looking at... Worst case scenario is that SUM=1 and the closest numbers are very far away, so O(inputLength*biggestInput)?
# As in (-9999, 10000)
# And what I did here is, let's see... Preparing partial sums is O(n), getting congruent groups is O(n), searching for
# candidates is O(m), m<=n; specific candidate list is O(p), p<=m; and finally getting the actual result is O(n*p)
# Sooooooo... O(n^2)... I guess that's kinda better, but that depends on input. Welp, premature optimisation and all that.
# Turns out I had an idea for an elegant solution, and came up with a sort of... Clever one? Not sure at this point.
# Anyway, lesson learned, let's not overcomplicate.

#####


def prepare_partial_sums(number_list):
    initial_partial_sums = list()
    partial_sum = 0
    for number in number_list:
        partial_sum += int(number)
        initial_partial_sums.append(partial_sum)

    total = partial_sum
    return initial_partial_sums, total


def prepare_congruent_groups(partial_sums, total):
    grouped_partial_sums = dict()
    for number in partial_sums:
        remainder = number % total if total != 0 else number
        if not remainder in grouped_partial_sums:
            grouped_partial_sums[remainder] = list()

        grouped_partial_sums[remainder].append(
            math.floor(number/(total if total != 0 else 1)))
    return grouped_partial_sums


def find_candidates(grouped_partial_sums):
    candidate_pairs = dict()
    smallest_step = -1  # would be nice to get the first pair straight away
    for key in grouped_partial_sums:
        grouped_partial_sums[key].sort()
        last_value = -1  # same
        for value in grouped_partial_sums[key]:
            if (last_value == -1):
                last_value = value
                continue
            step = value - last_value
            if (smallest_step == -1):
                smallest_step = step
            if (step < smallest_step):
                candidate_pairs.clear()
                smallest_step = step
            if (step == smallest_step):
                if not key in candidate_pairs:
                    candidate_pairs[key] = list()
                print("before ", candidate_pairs)
                candidate_pairs[key].append([last_value, value])
                print("after ", candidate_pairs)
            last_value = value
    return candidate_pairs, smallest_step


def get_specific_candidates(candidate_pairs, sum):
    candidates = []
    for key in candidate_pairs:
        for pair in candidate_pairs[key]:
            candidates.append(key + sum*(pair[0] if sum < 0 else pair[1]))
    return candidates


def find_first_occurence(candidates, partial_sums):
    return next(number for number in partial_sums if number in candidates)


def find_first_partial_sum_duplicate(number_list):
    # # Brute force approach. Not very elegant... But ten times shorter (counting lines of code)!
    # previouslyFoundNumbers = set()
    # sum = 0
    # while True:
    # 	for number in number_list:
    # 		sum = sum + int(number)
    # 		# print(str(len(previouslyFoundNumbers)) + " " + str(sum))
    # 		if (sum in previouslyFoundNumbers):
    # 			return sum
    # 		previouslyFoundNumbers.add(sum)

    # Prepare partial sums
    print("Input: ", number_list)
    initial_partial_sums, total = prepare_partial_sums(number_list)
    print("Partial sums: ", initial_partial_sums)
    print("Total: ", total)

    # if total == 0:
    # 	special case, need to sort the partial sums and check for duplicates
    # 	return

    # Prepare congruent groups
    grouped_partial_sums = prepare_congruent_groups(
        initial_partial_sums, total)

    # now the groups would likely need to be checked for duplicates... Or should
    # they? the generic behaviour should point out duplicates quite easily
    print("Grouped partial sums: ", grouped_partial_sums)
    for key in grouped_partial_sums:
        print(key, grouped_partial_sums[key])

    indices_to_delete = list()
    for key in grouped_partial_sums:  # i wonder if there's a kind of foreach that'd fit here
        if (len(grouped_partial_sums[key]) < 2):
            indices_to_delete.append(key)

    for key in indices_to_delete:
        del grouped_partial_sums[key]

    print("Trimmed partial sums: ", grouped_partial_sums)

    # good. Now, there are two (three) ways:
    # 1. There are groups with more than one member -> find candidates fot title of first dupe
    # 2. There are no such groups return false.
    # 2b. Unless the sum of input list is 0 - in that case we'll loop right back to it, free win

    if len(grouped_partial_sums) == 0:
        if (total == 0):
            return (True, 0)
        return (False, None)

    candidate_pairs, step = find_candidates(grouped_partial_sums)
    candidates = get_specific_candidates(candidate_pairs, total)

    result = find_first_occurence(
        candidates, [(number + step*total) for number in initial_partial_sums])

    return (True, result)
