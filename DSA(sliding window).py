#sliding window
#1.Example 1: Maximum Sum of k Consecutive Elements (Fixed-size window)
def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return "Invalid input"
    
    max_sum = sum(arr[:k])  # Initial sum of first window
    curr_sum = max_sum
    
    for i in range(k, n):
        curr_sum += arr[i] - arr[i - k]  # Slide window
        max_sum = max(max_sum, curr_sum)
    
    return max_sum

arr = [2, 1, 5, 1, 3, 2]
k = 3
print("Maximum sum of subarray of size", k, ":", max_sum_subarray(arr, k))

#2.Example 2: Longest Substring Without Repeating Characters (Variable-size window)
def longest_unique_substring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1  # Shrink the window
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

s = "abcabcbb"
print("Length of longest unique substring:", longest_unique_substring(s))
