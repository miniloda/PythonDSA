

def gcd(a,b):
  if b == 0:
    return a
  return (gcd(b, a%b))

n,m = input().split()
print(gcd(int(n), int(m)))