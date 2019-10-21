import functions
import pytest

from functions import Patch2D

data_parseInput = [
    pytest.param("#1 @ 432,394: 29x14", Patch2D(432, 394, 461, 408)),
    pytest.param("#2 @ 57,42: 12x16", Patch2D(57, 42, 69, 58)),
    pytest.param("#3 @ 138,913: 22x20", Patch2D(138, 913, 160, 933)),
    pytest.param("#4 @ 976,493: 24x21", Patch2D(976, 493, 1000, 514)),
    pytest.param("#5 @ 500,963: 12x16", Patch2D(500, 963, 512, 979)),
    pytest.param("#6 @ 737,354: 17x21", Patch2D(737, 354, 754, 375))
]


@pytest.mark.parametrize("word,result", data_parseInput)
def test_parseInput(word, result):
    assert result == functions.parseInput(word)


data_overlaps = [
    #
    # ++ xx
    # ++ xx
    #
    pytest.param(Patch2D(1, 1, 3, 3), Patch2D(4, 1, 6, 3), False),

    #
    # ++xx
    # ++xx
    #
    pytest.param(Patch2D(1, 1, 3, 3), Patch2D(3, 1, 5, 3), False),

    #
    #  xx
    # +#x
    # ++
    #
    pytest.param(Patch2D(1, 1, 3, 3), Patch2D(2, 2, 4, 4), True),

    #
    # ##
    # ##
    #
    pytest.param(Patch2D(1, 1, 3, 3), Patch2D(1, 1, 3, 3), True),

    #
    # +##
    # +##
    # +++
    #
    pytest.param(Patch2D(1, 1, 4, 4), Patch2D(2, 2, 4, 4), True),
]
@pytest.mark.parametrize("A,B,result", data_overlaps)
def test_overlaps(A, B, result):
    assert A.isOverlapping(B) == result


data_splitPatch = [
    #
    # +++
    # +#+
    # +++
    #   \/
    # ACB
    # AEB
    # ADB
    #
    pytest.param(Patch2D(0, 0, 3, 3), Patch2D(1, 1, 2, 2),
                 [Patch2D(0, 0, 1, 3), Patch2D(2, 0, 3, 3),
                  Patch2D(1, 0, 2, 1), Patch2D(1, 2, 2, 3),
                  Patch2D(1, 1, 2, 2)])
]


def assertEq(patch1, patch2):
    x1, y1, x2, y2 = patch1.unpack()
    a1, b1, a2, b2 = patch2.unpack()
    assert [x1, y1, x2, y2] == [a1, b1, a2, b2]
    return [x1, y1, x2, y2] == [a1, b1, a2, b2]


@pytest.mark.parametrize("patch,splitBy,result", data_splitPatch)
def test_splitPatch(patch, splitBy, result):
    # assert set(functions.splitPatch(patch, splitBy)) == set(result)
    splitPatch = [p.unpack() for p in functions.splitPatch(patch, splitBy)]
    unpackedResult = [p.unpack() for p in result]

    assert set(splitPatch) == set(unpackedResult)


def test_findOverlaps():
    patch = Patch2D(1, 1, 2, 2)
    others = [Patch2D(0, 0, 2, 2), Patch2D(1, 1, 2, 2), Patch2D(5, 5, 6, 6)]
    result = [Patch2D(0, 0, 2, 2), Patch2D(1, 1, 2, 2)]

    assert set([p.unpack() for p in functions.findOverlaps(
        patch, others)]) == set([p.unpack() for p in result])


def test_insert():
    patch1 = Patch2D(1, 1, 2, 2)
    patch2 = Patch2D(0, 0, 3, 3)

    patchSet = set()
    overlapSet = set()

    functions.insert(patch1, patchSet, overlapSet)
    assert len(patchSet) == 1

    functions.insert(patch2, patchSet, overlapSet)
    assert len(patchSet) == 5
    assert len(overlapSet) == 1

    assert functions.getArea(patchSet) == 9
    assert functions.getArea(overlapSet) == 1

    # checking if another overlap breaks anything
    functions.insert(patch1, patchSet, overlapSet)
    assert len(patchSet) == 5
    assert len(overlapSet) == 1

    assert functions.getArea(patchSet) == 9
    assert functions.getArea(overlapSet) == 1
