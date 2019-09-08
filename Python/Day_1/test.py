
import functions

def test_sum_list():
    assert functions.sum_list([0]) == 0
    assert functions.sum_list([0, 1]) == 1
    assert functions.sum_list([5, 10]) == 15
    assert functions.sum_list([0, 1, -1]) == 0
    assert functions.sum_list([0, 8, -4, 8]) == 12

def test_find_duplicate():
    assert functions.find_first_partial_sum_duplicate(
        [0]) == (True, 0)
    assert functions.find_first_partial_sum_duplicate(
        [0, 1]) == (True, 1)
    assert functions.find_first_partial_sum_duplicate(
        [0, 1, -1]) == (True, 0)
    assert functions.find_first_partial_sum_duplicate(
        [0, 8, -4, 8]) == (True, 8)

    assert functions.find_first_partial_sum_duplicate(
        [5, 10]) == (False, None)
