class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_hash_table = {}
        key_hash_table = {}
        if len(list(pattern)) != len(s.split(" ")): return False
        for word, key in zip(s.split(" "), list(pattern)):
            if word not in word_hash_table:
                word_hash_table[word] = key
            if key not in key_hash_table:
                key_hash_table[key] = word
            if key != word_hash_table[word] or word != key_hash_table[key]: return False
        
        return True