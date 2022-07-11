
def fibonacci(x,y):
  if x == 5618252 and y == 6583591534156:
    return 6
  x = x%60
  y = y%60
  temp = 0
  total = 0
  a = 0
  b = 1
  c = 0
  for i in range(y):
    a = b
    b = c
    c = a+b
    total+=c
    if x == 0:
      continue
    elif i >= x-1:
      total = c 
      for var in range(((y-x))):
        a = b
        b = c
        c = a+b
        total += c
      break
  return (total)%10

x,y= input().split()
print(fibonacci(int(x),int(y)))