def consecutive_ducks(n):
    while n > 1:
        if n % 2 == 1:
            return True
        n = n // 2
    return False

print(consecutive_ducks(522))



