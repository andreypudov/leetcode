import unittest

from problems.problem_10 import Solution, Token


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_isMatchs(self):
        self.assertFalse(self.solution.isMatch("aa", "a"))
        self.assertTrue(self.solution.isMatch("aa", "a*"))
        self.assertTrue(self.solution.isMatch("ab", ".*"))
        self.assertTrue(self.solution.isMatch("aab", "c*a*b"))
        self.assertTrue(self.solution.isMatch("aaa", "ab*ac*a"))
        self.assertTrue(self.solution.isMatch("mississippi", "mis*is*ip*."))
        self.assertFalse(self.solution.isMatch("mississippi", "mis*is*p*."))
        self.assertTrue(self.solution.isMatch("ac", ".*c"))
        self.assertTrue(self.solution.isMatch("aaa", "a*a"))
        self.assertTrue(self.solution.isMatch("aaa", "ab*a*c*a"))
        self.assertTrue(self.solution.isMatch("mississippi", "m.*si*pp."))

    def test_tokenize(self):
        self.assertEqual(self.solution.tokenize("a"), [Token("a", False)])
        self.assertEqual(self.solution.tokenize("a*"), [Token("a", True)])
        self.assertEqual(self.solution.tokenize(".*"), [Token(".", True)])
        self.assertEqual(
            self.solution.tokenize("ab"), [Token("a", False), Token("b", False)]
        )
        self.assertEqual(
            self.solution.tokenize("c*a*b"),
            [Token("c", True), Token("a", True), Token("b", False)],
        )
        self.assertEqual(
            self.solution.tokenize("ab*ac*a"),
            [
                Token("a", False),
                Token("b", True),
                Token("a", False),
                Token("c", True),
                Token("a", False),
            ],
        )


if __name__ == "__main__":
    unittest.main()
