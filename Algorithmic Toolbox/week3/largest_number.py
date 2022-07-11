#Uses python3

import sys


def largest_number(a):
    res = ""
    i = 0
    while len(a) > 0:
        i = i+ 1
        safe_max = find_max_number(a)
        res += safe_max
        a.remove(safe_max)

    return res

def find_max_number(a):
    maximum = a[0]
    for x in a:
        temp1 = str(maximum) + str(x)
        temp2 = str(x) + str(maximum)
        if temp1>temp2: pass
        else: maximum = x
    return maximum

    

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    