#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    num_argv = len(argv) - 1

    if num_argv == 0:
        print("0 arguments.")
    else:
        if num_argv == 1:
            print("1 argument:")
        else:
            print(f"{num_argv} arguments:")

        for i in range(1, len(argv)):
            print(f"{i}: {argv[i]}")
