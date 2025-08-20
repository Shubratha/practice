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


# using defaultdict

from collections import defaultdict


def top_most_common(events, k):
    event_dict = defaultdict(int)
    for event in events:
        event_dict[event] += 1

    ordered_events = list(sorted(event_dict.items(), key=lambda item: item[1], reverse=True))

    return ordered_events[:k]


events = ["click", "view", "click", "buy", "view", "click", "login"]
print(top_most_common(events, 2))