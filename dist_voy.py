class Solution:
    def countVowels(self,s):
        vowel=['a','e','i','o','u','A','E','O','U','I']
        dist = {}
        for x in s:
            if x in vowel:
                dist[x] = x
        val = len(dist.keys())
        return val
        #code here
