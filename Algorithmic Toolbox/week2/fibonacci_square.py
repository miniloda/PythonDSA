
def fibonacci(n):
  n = n%60
  total = 0
  temp = 0
  a = 0
  b = 1
  c = 0
  for i in range(n+1):
    a = b
    b = c
    if i == n:
      temp = c
    c = a+b
  return ((temp%10)*(c%10))%10

n= input()
print(fibonacci(int(n)))