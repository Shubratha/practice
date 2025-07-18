"""
You're in a ski tournament, where you ski from top of the mountain to one of the
finish checkpoints at the bottom. There are multiple routes with checkpoints
(each checkpoint has an associated point with it). And your total score =
(points from all checkpoints you visited - time of your travel).

Given: A List of lists, that consists [start_cp, end_cp, time_to_travel]
       A list of lists, that consists [cp, point]
Goal: Find the maximum score that you can collect during the tournament and print
out the optimal path.


                 START[0]
                  / | \
                 5  6  10
                /   |   \
             A[24] B[3] C[10]
                \   |   /|
                 4  5  6 5
                  \ | /  |
                   D[7] E[24]
                     \   |
                      3  1
                       \ |
                        F[3]
                        / \
                       5  10
                      /     \
                  END_1[4]  END_2[7]
Ruby/Python/js

0 -> A -> D -> F -> 1
(24 - 5) + (7 - 4) + (3-3) + (4-5) = 21  = ans

0 -> B -> D -> F -> 2
(3-6) -> (7-5) + (3-3) + (7-10) = -8


travel_time = [
    ["START", "A", "5"],
    ["START", "B", "6"],
    ["START", "C", "10"],
    ["A", "D", "4"],
    ["B", "D", "5"],
    ["C", "D", "6"],
    ["C", "E", "5"],
    ["D", "F", "3"],
    ["E", "F", "1"],
    ["F", "END_1", "5"],
    ["F", "END_2", "10"],
]
points = [
    ["START", "0"],
    ["A", "24"],
    ["B", "3"],
    ["C", "10"],
    ["D", "7"],
    ["E", "24"],
    ["F", "3"],
    ["END_1", "4"],
    ["END_2", "7"],
]
"""

# # ["START", "A", "D", "F"]
# # ["START", "B", ]
# {"START": ["A", "B", "C"], "A": ["D"]}
#
# connections = {}  # (checkpoint, dist, score)
# point_mappings = {}
#
#
# def get_path_score(route: list, score):
#     print("get_path_score", route, score)
#     for r in connections[route[0]]:  # [('D', 4, 7)], 'B': [('D', 5, 7)]
#         print(r)
#         if "END" in r[0]:
#             return score
#         tmp_score = score
#         tmp_score += get_path_score(connections[r[0]], tmp_score)
#         # [('F', 3, 3)]
#
#     score += route[2] - route[1]
#
#
# def find_max_score(travel_time: list, points: list) -> int:
#     starting_point, ending_point = "START", "END"
#     for point in points:
#         point_mappings[point[0]] = int(point[1])
#     for checkpoint in travel_time:
#         if checkpoint[0] in connections:
#             connections[checkpoint[0]].append((checkpoint[1], int(checkpoint[2]), point_mappings[checkpoint[1]]))
#         else:
#             connections[checkpoint[0]] = [((checkpoint[1], int(checkpoint[2]), point_mappings[checkpoint[1]]))]
#
#     print(connections)
#
#     max_score = 0
#
#     # for cp, paths in connections.items():
#     for route in connections[starting_point]:
#         cur_score = 0
#         # for route in paths:
#         #     print(route)
#         cur_score = get_path_score(route, cur_score)
#         max_score = max(max_score, cur_score)
#
#     return max_score
#
#
# max_score = find_max_score(travel_time, points)
# print(max_score)

from typing import List, Tuple
from collections import defaultdict

connections = defaultdict(list)
point_mappings = {}

def get_path_score(node: str, current_score: int) -> int:
    # If we reached an end node
    if node.startswith("END"):
        return current_score + point_mappings.get(node, 0)

    max_path_score = float('-inf')

    for neighbor, travel_time, neighbor_score in connections.get(node, []):
        # Calculate score for taking this path
        score_after_move = current_score + point_mappings.get(node, 0) + neighbor_score - travel_time
        # Recurse
        total = get_path_score(neighbor, current_score + point_mappings.get(node, 0) - travel_time)
        max_path_score = max(max_path_score, total)

    return max_path_score

def find_max_score(travel_time: List[List[str]], points: List[List[str]]) -> int:
    connections.clear()
    point_mappings.clear()

    for point in points:
        point_mappings[point[0]] = int(point[1])

    for u, v, t in travel_time:
        connections[u].append((v, int(t), point_mappings.get(v, 0)))

    max_score = float('-inf')
    for v, t, vscore in connections["START"]:
        initial_score = point_mappings["START"] + vscore - t
        total = get_path_score(v, point_mappings["START"] - t)
        max_score = max(max_score, total)

    return max_score