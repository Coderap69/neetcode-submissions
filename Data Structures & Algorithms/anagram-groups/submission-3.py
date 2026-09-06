class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = defaultdict(list)
        for i in strs:
            myarray = [0]*26
            for j in i:
                myarray[ord(j)-97]+=1
            key = tuple(myarray)
            result_dict[key].append(i)
        result_array = [result_dict[i] for i in result_dict]
        return result_array
        