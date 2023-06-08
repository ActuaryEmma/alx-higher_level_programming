#!/usr/bin/python3
import sys
total = 0
length = len(sys.argv)
# if only one argument or no argument
if (length <= 1):
    print("0")
else:
    for i in range(1, length):
        for j in range(len(sys.argv[i])):
			#if not a digit
            if not sys.argv[i][j].isdigit():
                print("Error")
                sys.exit()
        #add the integer in the command line		
        total += int(sys.argv[i])
    print("{}".format(total))	
    
