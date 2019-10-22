import sys
import time
import math


def solve(polymer):
    # print(len(polymer))
    return len(reducePolymer(polymer.strip()))


def solve2(polymer):
    reduced = ''.join(reducePolymer(polymer.strip()))

    # i think this would be a nice place for a lambda min(res for range())
    bestPolymerLen = len(reduced)
    print(bestPolymerLen)
    for char in range(ord('a'), ord('z')+1):
        improvedPolymer = reduced.replace(
            chr(char), '').replace(chr(char).upper(), '')
        bestPolymerLen = min(
            len(reducePolymer(improvedPolymer)), bestPolymerLen)
    return bestPolymerLen


def reducePolymer(polymer):
    result = []
    for char in polymer:
        # print(char, result)
        if len(result) > 0:
            lastChar = result[-1:][0]
            if int(math.fabs(float(ord(lastChar) - ord(char)))) == 32:
                result.pop()
            else:
                result.append(char)
        else:
            result.append(char)
    # print("Result: ", result)
    return result
# doesn't seem to be working, lets test it a little and see what's wrong


def main():
    runMain = True
    if runMain:
        with open('input.sdx') as file_object:
            contents = file_object.readline()
            start = time.time()
            polymerLen = solve(contents)
            print("Part 1 solution: " + str(polymerLen) +
                  " found in " + str(time.time() - start))
            start = time.time()
            bestPolymerLen = solve2(contents)
            print("Part 2 solution: " + str(bestPolymerLen) +
                  " found in " + str(time.time() - start))

    assert solve("""aaaAAB
    """) == 2
    assert solve("""aaaAAA
    """) == 0
    assert solve("""dabAcCaCBAcCcaDA
    """) == 10


if __name__ == '__main__':
    main()
