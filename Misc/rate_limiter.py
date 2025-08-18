"""
Basic Fixed Window Rate Limiter
Features:
	•	add(user_id): register a request
	•	allow(user_id): returns True if user is allowed under rate limit
	•	Customize: max_requests per window_seconds
"""

import time
from collections import defaultdict, deque

class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window = window_seconds
        self.user_requests = defaultdict(deque)  # user_id -> deque of timestamps

    def allow(self, user_id: str) -> bool:
        now = time.time()
        window_start = now - self.window
        dq = self.user_requests[user_id]

        # Remove outdated timestamps
        while dq and dq[0] < window_start:
            dq.popleft()

        if len(dq) < self.max_requests:
            dq.append(now)
            return True
        else:
            return False


rl = RateLimiter(max_requests=3, window_seconds=10)

for i in range(5):
    allowed = rl.allow("user1")
    print(f"Request {i+1}: {'✅ allowed' if allowed else '❌ rate-limited'}")
    time.sleep(2)
