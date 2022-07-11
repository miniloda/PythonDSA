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
    
    total+=c
  return (total)%10

n= input()
print(fibonacci(int(n)))