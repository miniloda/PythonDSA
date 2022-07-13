#Task. Find the first occurence of an integer in the given sorted sequence of integers (possibly with dupli-
#cates).

def binary_search_with_duplicates(keys, query):# FIXME: fails some test
    """_summary_

    Args:
        keys (list): A list of integers
        query (int): An integer to search for in the given sorted sequence of integers

    Returns:
        integer: The index of the first occurence of the given integer in the given sorted sequence of integers
    """
    low = 0
    high = len(keys)-1
    while True:
        if high < low:
            return -1
        mid = low + ((high-low) // 2)
        while query == keys[mid]:
            if query == keys[mid-1]:
                mid -= 1
            else:
                return mid
        if query > keys[mid]:
            low = mid+1
        else:
            high = mid-1


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search_with_duplicates(input_keys, q), end=' ')
