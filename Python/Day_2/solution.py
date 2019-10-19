import sys
import functions

def main():
	print(sys.path)
	with open('input.txt') as file_object:
		contents = file_object.read().rsplit()
		print("Part 1 solution (checksum of word list): " + str(functions.countChecksum(contents)))
		print("Part 2 solution : ")


if __name__ == '__main__':
    main()