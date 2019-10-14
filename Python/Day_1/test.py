
import functions

def test_sum_list():
    assert functions.sum_list([0]) == 0
    assert functions.sum_list([0, 1]) == 1
    assert functions.sum_list([5, 10]) == 15
    assert functions.sum_list([0, 1, -1]) == 0
    assert functions.sum_list([0, 8, -4, 8]) == 12

def prepare_partial_sums_util(list, expected_sum, expected_partial_sums):
    partial_sums, sum = functions.prepare_partial_sums(list)
    assert expected_partial_sums == partial_sums
    assert expected_sum == sum

def test_prepare_partial_sums():
    prepare_partial_sums_util(
        [0],
        0,
        [0]
    )

    prepare_partial_sums_util(
        [0, 1],
        1,
        [0, 0]
    )

    prepare_partial_sums_util(
        [1, -1],
        0,
        [0, 1]
    )
    
    prepare_partial_sums_util(
        [8, -4, 8],
        12,
        [0, 8, 4]
    )

def test_prepare_congruent_groups():
    res = functions.prepare_congruent_groups([1,2,3,4,5,6,7], 4)
    assert res == {
        0: [4],
        1: [1, 5],
        2: [2,6],
        3: [3, 7]}

    res = functions.prepare_congruent_groups([1,1,5], 4)
    assert res == {
        1: [1, 1, 5]}


def test_find_candidates():
    res = functions.find_candidates({0: [1,2], 1: [1,2]})
    assert res == {
        0: [{1,2}],
        1: [{1,2}]
    }
    
# def test_find_duplicate():
#     assert functions.find_first_partial_sum_duplicate(
#         [0]) == (True, 0)
#     assert functions.find_first_partial_sum_duplicate(
#         [0, 1]) == (True, 1)
    # assert functions.find_first_partial_sum_duplicate(
    #     [1, -1]) == (True, 0)
#     assert functions.find_first_partial_sum_duplicate(
#         [0, 8, -4, 8]) == (True, 8)

    # assert functions.find_first_partial_sum_duplicate(
    #     [5, 10]) == (False, None)
