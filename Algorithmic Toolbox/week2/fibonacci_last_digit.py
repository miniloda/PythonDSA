
def fibonacci(n):
  n = n%60
  total = 0
  a = 0
  b = 1
  c = 0
  for i in range(n):
    a = b
    b = c
    c = a+b
  return c%10

c= input()
print(fibonacci(int(c)))