#!/usr/bin/python3
if __name__ == "__main__":
    """print the addition of all arguments."""
    from sys import argv

    sum = 0
    for i in range(len(argv) - 1):
        sum += int(argv[i + 1])
    print("{:d}".format(sum))
