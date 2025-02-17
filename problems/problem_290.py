# 290. Word Pattern
#
# Given a pattern and a string s, find if s follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in s. Specifically:
#
#     - Each letter in pattern maps to exactly one unique word in s.
#     - Each unique word in s maps to exactly one letter in pattern.
#     - No two letters map to the same word, and no two words map to the same
#       letter.


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping = {}
        words = s.split()

        if len(pattern) != len(words):
            return False

        for index in range(len(pattern)):
            key = pattern[index]
            value = words[index]

            if key in mapping or value in mapping.values():
                if mapping.get(key, None) == value:
                    continue
                else:
                    return False

            mapping[key] = value

        return True
