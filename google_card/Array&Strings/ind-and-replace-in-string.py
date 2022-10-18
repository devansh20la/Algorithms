class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        mydict = {}
        for i,j,k in zip(indices, sources, targets):
            mydict[i] = (j,k)
            
        i = 0
        res = ""
        while (i < len(s)):
            if i in mydict and s[i:].startswith(mydict[i][0]):
                res += mydict[i][1]
                i+=len(mydict[i][0])
            else:
                res += s[i]
                i+=1
            
        return res
                

                