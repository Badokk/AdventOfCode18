import sys
import functions


def main():
    print(sys.path)
    with open('input.txt') as file_object:
        contents = file_object.read().rsplit()
        print("Part 1 solution (checksum of word list): " +
              str(functions.countChecksum(contents)))
        sol2 = functions.findLargestCommonSubstring(contents)
        if sol2 == False:
            print("No valid solution for part 2 found.")
        else:
            print(
                "Part 2 solution (merge of the two least differing strings): " + str(sol2))


if __name__ == '__main__':
    main()
