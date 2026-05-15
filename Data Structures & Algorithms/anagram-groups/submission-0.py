class Solution:
 def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    map={}
    for s in strs:
        key = "".join(sorted(s))
        map[key]= map.get(key,[])
        map[key].append(s)
    return list(map.values())