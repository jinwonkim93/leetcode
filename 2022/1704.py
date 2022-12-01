class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        s = list(s)
        a = s[:len(s)//2]
        b = s[len(s)//2:]

        def isVowel(letter):
            vowels_dict = {"a" : True,
                        "e" : True,
                        "i" : True,
                        "o" : True,
                        "u" : True
                        }
            return vowels_dict.get(letter, False)
        
        return len(list(filter(isVowel, a))) == len(list(filter(isVowel, b)))


s1 = "book"
s2 = "textbook"
s3 = "TEXtBoOk"
solution = Solution()
assert solution.halvesAreAlike(s1) == True
assert solution.halvesAreAlike(s2) == False
assert solution.halvesAreAlike(s3) == False
