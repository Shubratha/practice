# https://leetcode.com/problems/pour-water/

"""
In this problem, we are provided with an elevation map represented by an array heights where each element heights[i] indicates the height of the terrain at index i. The width of each terrain column is 1. We are given a volume of water volume and a starting position k where the water starts to fall.

The water droplet will behave according to the following rules:

The water droplet initially falls onto the terrain or the water at index k.
The droplet then tries to move according to these conditions:
It flows to the left if it eventually would fall to a lower height.
If it can't move left, it flows to the right if it would eventually fall to a lower height in that direction.
If the droplet cannot move left or right to a lower height, it stays at its current position.
The term eventually fall indicates that there is a path for the droplet to reach a lower altitude than its current one by moving continuously in that direction. Water can only sit on top of terrain or other water, and it will always occupy a full index-width block. There are infinitely high walls on both sides of the array boundaries, hence water cannot spill outside the terrain array bounds.

The goal is to simulate the process of pouring volume units of water one by one at the index k and return the final distribution of water over the map.

Example:
heights = [2, 1, 1, 2, 1, 2]
volume = 4
k = 2 (the starting position for pouring water)

Answer: [2, 2, 3, 2, 2, 2]

"""

def pour_water(heights: list, volume: int, k: int):
    width = len(heights)
    for _ in range(volume):
        for d in (-1, 1):
            cur_pos = best_pos = k
            print(cur_pos, d)
            while 0 <= cur_pos + d < width and heights[cur_pos + d] <= heights[k]:
                if heights[cur_pos + d] < heights[k]:
                    best_pos = cur_pos + d
                cur_pos += d

            if best_pos != k:
                heights[best_pos] += 1
                break

        else:
            heights[k] += 1

    return heights
