def descendingOrder(n):
    # CONVERT NUMBER INTO AN ARRAY OF NUMBERS
    res = [int(x) for x in str(n)]
    # print(res)
    for i, x in enumerate(res):
        for j, z in enumerate(res):
            if(res[i] > res[j]):
                temp = res[i]
                res[i] = res[j]
                res[j] = temp
    print(res)

descendingOrder(25748)
