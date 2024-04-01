from typing import List

class Solution:
    def isDominating(self, arr: List[int]) -> bool:
        freq = {}  # key: element, value: frequency
        for el in arr:
            if el not in freq:
                freq[el] = 0
            freq[el] += 1
        max_freq = 0
        max_el = None
        for el, freq in freq.items():
            if freq > max_freq:
                max_freq = freq
                max_el = el
        return max_freq > len(arr) // 2