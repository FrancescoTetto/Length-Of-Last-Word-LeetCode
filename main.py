class Solution(object):
    def lengthOfLastWord(self, s):
        split_s = s.split()
        length_last_word = len(split_s[-1])

        return length_last_word

solution = Solution()
s = "Hello World"

print(solution.lengthOfLastWord(s))
