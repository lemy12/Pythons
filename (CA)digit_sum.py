def reverse(text):
  new = ''
  length = len(text)
  while(length>0):
    new += text[length-1]
  return new
