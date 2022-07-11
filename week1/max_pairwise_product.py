
def max_pairwise_product(numlist):
	#in this algorithm, we use the sorting technique so that the last two numbers give out the maximum pairwise product
	#you can use sorted method here but ill just use merge sort
	#While it is fast to use sorted(), it is good to know how to sort efficiently
	numlist = merge_sort(numlist)
	return int(numlist[-1]*numlist[-2])


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right
    return result

if __name__ == "__main__":
	numbers = [float(x) for x in str(input()).split()]
	print(max_pairwise_product(numbers))