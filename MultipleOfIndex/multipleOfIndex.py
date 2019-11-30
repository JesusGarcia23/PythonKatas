def multipleOfIndex(theArr):
    result = []
    for i in range(len(theArr)):
        if i != 0 and (theArr[i] % i) == 0:
            result.append(theArr[i])

    return result


print(multipleOfIndex([22, -6, 32, 82, 9, 25]))       
