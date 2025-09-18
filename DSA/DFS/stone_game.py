"""
You begin with a single heap of stones, initially containing n stones. During an operation, you have the option to perform the following:
Divide any pile into two separate piles, ensuring that one of the resulting piles contains precisely twice as many stones as the other.
Is it possible to create a pile containing exactly m stones using a series of the above-mentioned operations?

Example 1: n=9, m=4
Output: true. Breaks into 6,3 then 4,2. Thus true.

Example 2: n=3, m=3
Output: true

Example 3: n=72, m=15
Output: false

Example 4: n= 9, m =6
output : true
"""

def can_create_pile(n: int, m: int) -> bool:
    memo = {}

    def dfs(pile):
        if pile == m:
            return True
        if pile < m or pile % 3 != 0:
            return False
        if pile in memo:
            return memo[pile]

        one_third = pile // 3
        two_third = pile - one_third

        # Try both branches
        memo[pile] = dfs(one_third) or dfs(two_third)
        return memo[pile]

    return dfs(n)


# 	Time: O(U), where U = number of distinct pile sizes tried (realistically O(log n))
# 	Space: O(U) for memoization stack and cache
