# https://leetcode.com/problems/group-anagrams/

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams_dict = {}
        for s in strs:
            ss = self.sortString(s)
            if ss not in anagrams_dict:
                anagrams_dict[ss] = [s]
            else:
                anagrams_dict[ss] += [s]
        # print(anagrams_dict, anagrams_dict.values())
        return anagrams_dict.values()

    def sortString(self, str):
        return ''.join(sorted(str))
