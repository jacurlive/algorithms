# https://binarysearch.com/problems/Detect-Voter-Fraud
class Solution:
    def solve(self, votes):
        return len(set(list(zip(*votes))[1])) != len(votes)


votes_1 = [
    [3, 1],
    [3, 1],
    [3, 5]
]

s = Solution()
s.solve(votes_1)
