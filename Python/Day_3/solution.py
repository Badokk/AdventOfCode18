import sys
import functions
import time


def main():
    with open('input.txt') as file_object:
        contents = file_object.read().splitlines()
        start = time.time()
        result = functions.solve(contents)
        print("Part 1 solution (area of overlapping claims): " +
              str(result) + " found in " + str(time.time() - start))

        start = time.time()
        result = functions.solve_part2(contents)
        print("Part 2 solution (single non-overlapping claim): " +
              str(result) + " found in " + str(time.time() - start))


if __name__ == '__main__':
    main()
