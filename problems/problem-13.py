class Solution:
    # M - 1000
    # CM - 900
    # D - 500
    # CD - 400
    # C - 100,
    # XC - 90
    # L - 50,
    # XL - 40
    # X - 10,
    # IX - 9
    # V - 5,
    # IV - 4
    # I - 1
    def romanToInt(self, s: str) -> int:
        number = 0
        idx = 0
        while idx < len(s):
            next_pair = self.getNextToken(s, idx)
            if next_pair[0] == "M":
                number += 1000
                idx += 1
            elif next_pair == "CM":
                number += 900
                idx += 2
            elif next_pair[0] == "D":
                number += 500
                idx += 1
            elif next_pair == "CD":
                number += 400
                idx += 2
            elif next_pair[0] == "C":
                number += 100
                idx += 1
            elif next_pair == "XC":
                number += 90
                idx += 2
            elif next_pair[0] == "L":
                number += 50
                idx += 1
            elif next_pair == "XL":
                number += 40
                idx += 2
            elif next_pair[0] == "X":
                number += 10
                idx += 1
            elif next_pair == "IX":
                number += 9
                idx += 2
            elif next_pair[0] == "V":
                number += 5
                idx += 1
            elif next_pair == "IV":
                number += 4
                idx += 2
            elif next_pair[0] == "I":
                number += 1
                idx += 1
        return number

    def getNextToken(self, s, pos):
        lenght = len(s)
        if lenght - pos >= 2:
            return s[pos : pos + 2]
        else:
            return s[pos : pos + 1]
