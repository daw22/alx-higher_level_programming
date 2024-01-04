#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    length = len(sys.argv)
    nums = []
    for i in range(1, length):
        nums.append(int(sys.argv[i]))
    print("{:d}".format(sum(nums)))
