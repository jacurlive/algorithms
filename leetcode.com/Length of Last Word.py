# https://leetcode.com/problems/length-of-last-word/

def length_of_last_word(self, s: str) -> int:
    return len(s.strip().split(' ')[-1])
