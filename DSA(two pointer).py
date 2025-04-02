#two pointer
#1.Example 1: Find Two Numbers That Sum to a Target
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return (arr[left], arr[right])
        elif curr_sum < target:
            left += 1  # Increase sum
        else:
            right -= 1  # Decrease sum

    return "No pair found"

arr = [1, 2, 3, 4, 6, 8, 10]
target = 10
print("Pair with sum", target, ":", two_sum_sorted(arr, target))


#2.Example 2: Check If a String is a Palindrome
def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

s = "racecar"
print("Is palindrome?", is_palindrome(s))
