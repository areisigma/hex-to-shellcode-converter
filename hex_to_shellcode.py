import os
import sys

if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <hexcode>")
        exit(0)

hexcode=sys.argv[1]

def askForLittleEndian():
        x = input("Do you want an output to be little-endian? [y/n] ")
        if x == "y":
                return True
        else:
                return False


def parseLE(hex):
        shellStr = ""
        j = len(hex)

        for i in range(len(hex)):
                shellStr = shellStr + "\\x" + str(hex[j-2]) + str(hex[j-1])
                j = j - 2
                if i == (len(hex)/2)-1:
                        break

        return shellStr



def parse(hex):
        shellStr = ""

        for i in range(len(hex)):
                if (i+1)%2 != 0:
                        shellStr = shellStr + "\\x" + str(hex[i])
                else:
                        shellStr = shellStr + str(hex[i])
        return shellStr


if askForLittleEndian() == True:
        shellcode = parseLE(hexcode)
else:
        shellcode = parse(hexcode)

print(shellcode)