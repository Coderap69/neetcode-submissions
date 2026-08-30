class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mins = 201
        result = []
        minstring = ""
        z = 0
        for i in strs:
            if len(i)<mins:
                mins = len(i)
                minstring = i
        if(mins==0):
            return ""
        else:
            for i in range(len(minstring)):
                for j in strs:
                    if j[i]!=minstring[i]:
                        z = 1
                        break
                    else:
                        continue
                if z:
                    break
                result.append(minstring[i])
        restring = "".join(result)
        return restring
        