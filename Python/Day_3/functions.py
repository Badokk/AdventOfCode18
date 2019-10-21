import re
import queue

# Ok, what we will need:
# parseInput(word) string => ((int, int), (int, int))
# findOverlap(patch, patchSet) patch, patchSet => patchSet
# splitPatch(toSplit, splitBy) patch, patch => patch, patchSet

# And some smart data structure to make searching for overlaps easier. hmm... nah, regular set should do
# Sorting by one coord should be good enough. If I were to minimize lookup time I'd
# have to create two mirrored sets, but I don't think it's worth it


class Patch2D:
    def __init__(self, x1, y1, x2, y2):
        # x1,y1 is bottom left, x2,y2 is top right
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.x1 == other.x1 and self.y1 == other.y1 and self.x2 == other.x2 and self.y2 == other.y2

    def __hash__(self):
        return hash((self.x1, self.y1, self.x2, self.y2))

    def unpack(self):
        return self.x1, self.y1, self.x2, self.y2

    def isOverlapping(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        if self.x1 >= other.x2 or self.x2 <= other.x1:
            return False
        if self.y1 >= other.y2 or self.y2 <= other.y1:
            return False
        return True

    def getArea(self):
        return (self.x2 - self.x1) * (self.y2 - self.y1)


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.x == other.x and self.y == other.y


def solve(words):
    patchSet = set()
    overlapSet = set()

    for word in words:
        insert(parseInput(word), patchSet, overlapSet)

    return getArea(overlapSet)


def solve_part2(words):
    patchSet = set()
    overlapSet = set()

    for word in words:
        insert(parseInput(word), patchSet, overlapSet)

    counter = 0
    for word in words:
        counter += 1
        if len(findOverlaps(parseInput(word), overlapSet)) == 0:
            return counter


def parseInput(word):
    x, y, xdelta, ydelta = [int(s) for s in re.split(
        ' |,|: |x', word) if s.isdigit()]
    return Patch2D(x, y, x+xdelta, y+ydelta)


def insert(patch, patchSet, overlapSet):
    overlaps = findOverlaps(patch, patchSet)
    chunks = []
    chunks.append(patch)
    # counter = 0
    for chunk in chunks:
        subOverlaps = findOverlaps(chunk, overlaps)
        if len(subOverlaps) == 0:
            patchSet.add(chunk)
            continue

        splitChunks = splitPatch(chunk, subOverlaps[0])
        if len(splitChunks) == 1:
            if overlapSet != None:
                insert(splitChunks[0], overlapSet, None)
            continue
        for splitChunk in splitChunks:
            chunks.append(splitChunk)
    if len(chunks) == 1:
        return True
    return False

# huh. Looks sensible. Well, will see later


def getArea(patchSet):
    return sum(patch.getArea() for patch in patchSet)


def findOverlaps(patch, patchSet):
    result = [other for other in patchSet if patch.isOverlapping(other)]
    return result


def splitPatch(patch, splitBy):
    splitChunks = []
    # split by left x
    if isBetween(splitBy.x1, patch.x1, patch.x2):
        left = Patch2D(patch.x1, patch.y1, splitBy.x1, patch.y2)
        right = Patch2D(splitBy.x1, patch.y1, patch.x2, patch.y2)
        splitChunks.append(left)
        patch = right

    # split by right x
    if isBetween(splitBy.x2, patch.x1, patch.x2):
        left = Patch2D(patch.x1, patch.y1, splitBy.x2, patch.y2)
        right = Patch2D(splitBy.x2, patch.y1, patch.x2, patch.y2)
        splitChunks.append(right)
        patch = left

    # split by bot y
    if isBetween(splitBy.y1, patch.y1, patch.y2):
        bot = Patch2D(patch.x1, patch.y1, patch.x2, splitBy.y1)
        top = Patch2D(patch.x1, splitBy.y1, patch.x2, patch.y2)
        splitChunks.append(bot)
        patch = top

    # split by top y
    if isBetween(splitBy.y2, patch.y1, patch.y2):
        bot = Patch2D(patch.x1, patch.y1, patch.x2, splitBy.y2)
        top = Patch2D(patch.x1, splitBy.y2, patch.x2, patch.y2)
        splitChunks.append(top)
        patch = bot

    splitChunks.append(patch)
    return splitChunks
    # this looks ugly, but it gets the job done. I'd say, leave it


def isBetween(val, cmp1, cmp2):
    return (val > cmp1 and val < cmp2) or (val < cmp1 and val > cmp2)

# now that I've run it, it doesn't seem very fast...
# part two requires numbers for the patches...
