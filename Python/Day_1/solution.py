import sys
import functions


def main():
    print(sys.path)
    with open('input.txt') as file_object:
        contents = file_object.read().rsplit()
        print("Part 1 solution (sum of all list elements): " +
              str(functions.sum_list(contents)))
        print("Part 2 solution (first duplicate): " +
              str(functions.find_first_partial_sum_duplicate(contents)))


if __name__ == '__main__':
    main()
