import sys
import time
import math
import numpy as np
import re
import operator


BLANK_CELL = -1
TIED_CELL = -2


def solve(coords):
    parsed = parseInput(coords)
    norm = normalize(parsed)
    arrSize = getArrSize(norm)

    arr = [[BLANK_CELL for i in range(arrSize['y']+1)]
           for j in range(arrSize['x']+1)]

    arr = fillArray(arr, norm)
    result = getLargestArea(arr)
    return(result)


def parseInput(lines):
    coords = []
    for line in lines:
        x, y = re.findall(r"([0-9]+)", line)
        coords.append([int(x), int(y)])
    return coords


def getArrSize(coords):
    xs, ys = zip(*coords)
    return {'x': max(xs), 'y': max(ys)}


def normalize(coords):
    xs, ys = zip(*coords)
    return [[x, y] for x, y in zip(map(lambda x: x-min(xs), xs), map(lambda y: y-min(ys), ys))]


def fillArray(array, coords):
    queue = {}
    filledCells = 0
    for i, coord in enumerate(coords):
        queue[(coord[0], coord[1])] = i

    while len(queue) > 0:
        newQueue = {}
        for [x, y] in queue:
            i = queue[x, y]
            neighbors = [[a, b] for [a, b] in getNeighborCoords(
                x, y, array) if notFilled(a, b, array)]

            for x, y in neighbors:
                if (x, y) in newQueue and newQueue[x, y] != i:
                    newQueue[x, y] = TIED_CELL
                else:
                    newQueue[x, y] = i
        for [x, y] in newQueue:
            array[x][y] = newQueue[x, y]
            filledCells += 1
        queue.clear()
        queue = newQueue
    return array


def notFilled(x, y, array):
    return array[x][y] == BLANK_CELL


def getNeighborCoords(x, y, array):
    return [[i, j] for i, j in [[x, y-1], [x, y+1], [x-1, y], [x+1, y]] if inBounds(i, j, array)]


def inBounds(row, col, array):
    if row < 0 or col < 0:
        return False
    if row > len(array)-1 or col > len(array[0])-1:
        return False
    return True


def printArray(array):
    print("Array: ")
    for row in array:
        print(row)


def getLargestArea(array):
    ignoredLabels = set([array[i][j] for i in range(0, len(array)) for j in range(0, len(array[0])) if i in [0, len(
        array)-1] or j in [0, len(array[0])-1]])
    ignoredLabels.add(TIED_CELL)
    scores = {}
    for i in range(1, len(array)-1):
        for j in range(1, len(array[0])-1):
            if array[i][j] in ignoredLabels:
                continue
            if not array[i][j] in scores:
                scores[array[i][j]] = 1
            else:
                scores[array[i][j]] += 1
    return max(scores.values())


def main():
    runMain = True
    if runMain:
        with open('input.sdx') as file_object:
            contents = file_object.read().splitlines()
            start = time.time()
            print("Part 1 solution (largest area): " + str(solve(contents)) +
                  " found in " + str(time.time() - start))
            # start = time.time()
            # bestPolymerLen = solve2(contents)
            # print("Part 2 solution: " + str(bestPolymerLen) +
            #       " found in " + str(time.time() - start))
    else:
        parsed = parseInput(["1, 1",
                             "1, 6",
                             "8, 3",
                             "3, 4",
                             "5, 5",
                             "8, 9"])

        print("Parsed: ", parsed)
        norm = normalize(parsed)
        print("Normalized: ", norm)
        arrSize = getArrSize(norm)
        print("Arr size: ", arrSize)

        arr = [[BLANK_CELL for i in range(arrSize['y']+1)]
               for j in range(arrSize['x']+1)]
        printArray(arr)

        arr = fillArray(arr, norm)
        result = getLargestArea(arr)
        print(result)


if __name__ == '__main__':
    main()
