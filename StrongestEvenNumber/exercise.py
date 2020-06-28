def strongest_even(n, m, actualCounter = 0, strongest = 0):
  theNumber = n
  counter = 0
  newCounter = actualCounter
  newStrongest = strongest
  while theNumber % 2 == 0 and theNumber != 0:
    theNumber = theNumber / 2
    counter += 1

  if(counter > newCounter):
    newCounter = counter
    newStrongest = n
  if(n+1 <= m):
    return strongest_even(n+1, m, newCounter, newStrongest)
  elif(n >= m):
    return newStrongest


print(strongest_even(129, 193))


## RECURSIVE