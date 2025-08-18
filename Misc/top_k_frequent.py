"""
Given a list of events (or action codes), return the top K most frequent items.
"""

from collections import Counter


def top_k_frequent(events, k):
    freq = Counter(events)
    return [item for item, _ in freq.most_common(k)]


events = ["click", "view", "click", "buy", "view", "click", "login"]
k = 2
print(top_k_frequent(events, k))  # ➤ ['click', 'view']
