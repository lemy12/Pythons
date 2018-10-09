def remove_duplicates(elements):
  new = elements.copy()
  for each in new:
    for x in range(1, new.count(each)):
      new.remove(each)
  return new

print (remove_duplicates([3,1,1,2,2,1,2,2,3]))
