# Input: A series of strings
# Output: x*y, where
#   x = number of strings with a character that occurs twice
#   y = number of strings with a character that occurs thrice


def analiseWord(word):
    word = sorted(word)

    # Now, options are:
    # - iterate over the word with a counter
    # - cut string into pieces
    has_two_of_a_kind = False
    has_three_of_a_kind = False
    uniqueCharacters = set(word)
    for char in uniqueCharacters:
        count = word.count(char)
        if count == 2:
            has_two_of_a_kind = True
        if count == 3:
            has_three_of_a_kind = True

    return has_two_of_a_kind, has_three_of_a_kind


def countWordsWithDoubleAndTripleChars(words):
    doubles = 0
    triples = 0
    for word in words:
        has_two, has_three = analiseWord(word)
        doubles += int(has_two)
        triples += int(has_three)

    return doubles, triples


def countChecksum(words):
    doubles, triples = countWordsWithDoubleAndTripleChars(words)
    return doubles*triples


# Part two
# Input: A series of strings
# Output: Two strings that differ by a single character (in a single position!)
# Hmm, that's an interesting one. Brute force is O(n^2*m)
#
# Ok, I think I get it. If a distance between two strings == 1,
# then their distance against any other string can only differ by 1
# So. I'll take the first word and compate it against all others
# Then, I'll order the other words by number of differing chars
# Finally, I'll recurse the procedure for subgroups differing by 1
# 2-3, 3-4, 4-5 etc.

# Step 1: create distance map;
# Step 2: create subset to check
# Step 3: repeat

# How much better is this solution? Well, it depends on
# the length of the words and their relative randomness.
# If we assume the words are completely random, the comparison against
# one random word should be somewhat similar to a bell curve
# so the largest subset (10,11 distance with 20 char word)
# should be about 60-70% of the starting set. The complexity is still
# O(n^2*m), but closer to... E(k->inf) nm*(0.7)^k so substantially smaller

def findLargestCommonSubstring(words):
    result = findWordsDifferingByOne(words)
    if result != False:
        return ''.join([a for a, b in zip(result[0], result[1]) if a == b])

    return False


def findWordsDifferingByOne(words):
    distance_map = createDistanceMap(words)

    # handle special case here - only pivot is in map
    if len(distance_map) == 1:
        return False

    if 1 in distance_map:
        return distance_map[0][0], distance_map[1][0]
    for key in distance_map:
        if not key+1 in distance_map:
            continue
        subresult = findWordsDifferingByOne(
            distance_map[key] + distance_map[key+1])
        if subresult == False:
            continue
        return subresult

    return False


def createDistanceMap(words):
    distance_map = dict()
    pivot = words[0]
    distance_map[0] = [pivot]

    for word in words[1:]:
        differences = sum(1 for a, b in zip(pivot, word) if a != b)
        if not differences in distance_map:
            distance_map[differences] = list()
        distance_map[differences].append(word)
    return distance_map
