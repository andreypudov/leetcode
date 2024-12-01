# 383. Ransom Note
# Given two strings ransomNote and magazine, return true if ransomNote can be
# constructed by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = sorted(ransomNote)
        magazineMap = sorted(magazine)

        r_index = 0
        m_index = 0

        while r_index < len(ransomNote) and m_index < len(magazineMap):
            if ransomNote[r_index] == magazineMap[m_index]:
                r_index += 1

            m_index += 1

        return r_index == len(ransomNote)
