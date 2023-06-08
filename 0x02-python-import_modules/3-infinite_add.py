#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    total = 0
    length = len(sys.argv)
    # if only one argument or no argument
    if (length <= 1):
        print("0")
    else:
        for i in range(1, length):
            try:
                total += int(sys.argv[i])
            except ValueError:
                print("Error: Invalid input")
                sys.exit()
        print("{}".format(total))
