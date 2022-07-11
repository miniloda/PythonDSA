

def fibonacci(n):
  n = n%60
  a = 0
  b = 1
  c = 0
  for i in range(n):
    a = b
    b = c
    c = a+b
    
  return c

c= input()
print(fibonacci(int(c)))