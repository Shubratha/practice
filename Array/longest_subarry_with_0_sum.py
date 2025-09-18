"""
Find the length of the longest subarray that sums to 0 in a list of integers
 (which can include both positive and negative numbers)
"""

def get_longest_substring(nums):
    cur_sum, max_len = 0, 0
    num_dict = {}
    for i, n in enumerate(nums):
        cur_sum += n
        if cur_sum == 0:
            # max_len = max(max_len, i)
            max_len = i + 1

        elif cur_sum in num_dict:
            max_len = max(max_len, i - num_dict[cur_sum])
            # num_dict[cur_sum] = i
        else:
            num_dict[cur_sum] = i

    return max_len


print(get_longest_substring([-4, 3, 1, 5, -3, -2]))  # 6
print(get_longest_substring([15, -2, 2, -8, 1, 7, 10, 23]))  # 5
print(get_longest_substring([]))  # 0
print(get_longest_substring([15, 2]))  # 0
print(get_longest_substring([-2, 2, -3, 3]))  # 4