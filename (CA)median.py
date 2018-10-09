def median(numbers):
  new = sorted(numbers)
  length = len(new)
  middle = length//2
  if length%2==0:
    return (new[middle]+new[middle-1])/2
  else:
    return new[middle]

print (median([4,5,5,4]))
