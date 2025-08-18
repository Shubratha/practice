"""
Given a stream of numbers, support:

add(num)
get_max_last_k(k)
"""

from collections import deque


class StreamProcessor:
    def __init__(self):
        self.stream = deque()

    def add(self, num: int):
        self.stream.append(num)

    def get_max_last_k(self, k: int) -> int:
        if k > len(self.stream):
            raise ValueError("k exceeds the current stream size")

        max_val = float('-inf')
        for i in range(len(self.stream) - k, len(self.stream)):
            max_val = max(max_val, self.stream[i])
        return max_val


sp = StreamProcessor()
sp.add(5)
sp.add(3)
sp.add(10)
sp.add(7)
print(sp.get_max_last_k(2))  # ➤ 10
print(sp.get_max_last_k(3))  # ➤ 10