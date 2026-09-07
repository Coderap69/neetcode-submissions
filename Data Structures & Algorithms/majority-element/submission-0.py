class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dict = {}
        my_set = set()
        for i in nums:
            my_set.add(i)
        for i in my_set:
            count = 0
            for j in nums:
                if j==i:
                    count+=1
            my_dict[i] = count
        max_key = max(my_dict,key=my_dict.get)
        return max_key