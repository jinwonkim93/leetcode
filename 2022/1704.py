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
        print()

s1 = "book"
s2 = "textbook"
s3 = "TEXtBoOk"
solution = Solution()
solution.halvesAreAlike(s1)
solution.halvesAreAlike(s2)
solution.halvesAreAlike(s3)
