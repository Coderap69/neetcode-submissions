class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newList = nums.copy()
        for i in nums:
            newList.append(i)
        return newList