class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myDict = {}
        for i in s:
            if(myDict.get(i,0)==0):
                myDict.setdefault(i,1)
            else:
                myDict[i]+=1
        for i in t:
            if myDict.get(i,0)==0:
                return False
            else:
                myDict[i]-=1
        for i in myDict:
            if myDict[i]>0:
                return False
        return True