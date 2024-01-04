#!/usr/bin/python3
import sys
length = len(sys.argv)
if __name__ == "__main__":
    if length == 1:
        print("{:d} arguments.".format(length - 1))
    elif length == 2:
        print("{:d} argument:".format(length - 1))
    else:
        print("{:d} arguments:".format(length - 1))
    for i in range(1, length):
        print("{:d}: {:s}".format(i, sys.argv[i]))
