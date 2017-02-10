def internalPrint(count, msg):
    print("Count: {0}, Message: {1}".format(count, msg))

    
def printRecursively(count, msg):
    i = 0
    while count > i:
        internalPrint(i, msg)
        i += 1

def ExternalPrint():
    msgs = ("Apple", "Banana", "Orange")
    printCount = 5
    for msg in msgs:
        printRecursively(printCount, msg)
        printCount -= 1


if __name__ == '__main__':
    ExternalPrint()
