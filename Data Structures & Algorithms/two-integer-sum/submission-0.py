class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # dictionary: maps a number we've seen -> the index where we saw it

        for i, num in enumerate(nums):       # i = current index, num = value at that index
            difference = target - num         # the number we'd need to find to hit the target
            if difference in seen:            # have we already seen that needed number?
                return [seen[difference], i]  # yes! return its earlier index + current index
            seen[num] = i                     # no match yet — remember this number for later

        return []  # fallback (problem guarantees a valid answer exists, so this won't actually run)