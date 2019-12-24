def find_short(s):
    theStr = s.split(" ")
    theStr.sort(key=len)
    return len(theStr[0])