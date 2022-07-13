#Task. Find the first occurence of an integer in the given sorted sequence of integers (possibly with dupli-
#cates).

def binary_search_with_duplicates(keys, query):
    """_summary_

    Args:
        keys (list): A list of integers
        query (int): An integer to search for in the given sorted sequence of integers

    Returns:
        integer: The index of the first occurence of the given integer in the given sorted sequence of integers
    """
    low = 0
    high = len(keys)-1
    """ Explanation:
    In this function, the first two conditions checks if the given query is higher than the key.
    If these two arent satisfied, then we know that the query is equal to the keys[mid]. However,
    since we know that there are duplicates, we must change the high to mid while keeping the low as is.
    The loop will then continue and checks the conditionals until we reach low == mid then we know that
    keys[mid] is the first occurence and we will return the index.
    """
    while True:
        if high < low:
            return -1
        mid = low + ((high-low) // 2)
        if query > keys[mid]:
            low = mid+1
        elif query < keys[mid]:
            high = mid-1
        elif low != mid:
            high = mid
        else:
            return mid

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search_with_duplicates(input_keys, q), end=' ')
