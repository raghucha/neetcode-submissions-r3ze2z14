import collections
class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:
            if (len(str1) != len(str2)):
                return False

            countS, countT = {}, {}

            for i in range(len(str1)):
                countS[str1[i]] = 1 + countS.get(str1[i], 0)
                countT[str2[i]] = 1 + countT.get(str2[i], 0)
            return countS == countT


        