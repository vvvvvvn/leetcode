class Solution:
    def maxScore(self, s: str) -> int:
        max = 0

        for i,x in enumerate(s):
            if s[:i+1] != s:
                print(f'left: {s[:i+1]}')
                print(f'right: {s[i+1:]}')
                temp_max = s[:i+1].count('0') + s[i+1:].count('1') 
                max = temp_max if temp_max > max else max

        return max
if __name__ == '__main__':
    s = "011101"
    sol = Solution()
    print(sol.maxScore(s))