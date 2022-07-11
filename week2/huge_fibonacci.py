
def fibonacci(x,y):
  if x > y:
    i = 0
    a = 0
    b = 1
    c = 0
    lst = []
    while(True):
      i+=1
      a = b
      b = c
      c = a+b
      lst.append(c%y)
      if len(lst) > 2:
        if lst[-2] == 0 and lst[-1] == 1:
          i-=1
      
          break
    a = 0
    b = 1
    c = 0
    for var in range(x%i):
      a = b
      b = c
      c = a+b
    return c%y
  else:
    a = 0
    b = 1
    c = 0
    for i in range(x):
      a = b
      b = c
      c = a+b
    return c%y
x,y= input().split()
print(fibonacci(int(x),int(y)))