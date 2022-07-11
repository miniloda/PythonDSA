# Uses python3
import sys

def lcm_good(a, b):

    return  int((a*b)/(gcd(a,b)))

    return a*b
def gcd(a,b):
  if b == 0:
    return a
  return (gcd(b, a%b))
  
a,b = input().split()
print(lcm_good(int(a),int(b)))