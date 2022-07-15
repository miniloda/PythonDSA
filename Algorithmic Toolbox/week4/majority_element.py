# Uses python3
import sys

def get_majority_element(a, i, j):
    def count(a,i,j,c):
        res = 0;
        for k in range(i,j):
            if a[k] == c:
                res += 1
        return res
    if i == j:
        return -1
    if i+1 == j:
        return a[i]
    mid = (i + j-1)//2
    left = get_majority_element(a, i, mid + 1)
    right = get_majority_element(a, mid +1 , j)
    if count(a,i,j, left) > (j-i)//2:
        return left
    elif (j-1)//2 < count(a,i,j, right):
        return right
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, len(a)) != -1:
        print(1)
    else:
        print(0)
