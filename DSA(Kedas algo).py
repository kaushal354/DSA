#kedans algo:-
def max_subarray_sum(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]

    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

arr = [3,-4,5,4,-1,7,-8]
print(max_subarray_sum(arr))  # Output: 6 (subarray: [4, -1, 2, 1])
