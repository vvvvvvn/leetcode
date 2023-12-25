class Solution:
    def minOperations(self, s: str) -> int:
        count = 0
        count2 = 0
        for i, n in enumerate(s):
            if i % 2 == 0 and n != '0':
                count += 1
            elif i % 2 != 0 and n != '1':
                count += 1

            if i % 2 == 0 and n != '1':
                count2 += 1
            elif i % 2 != 0 and n != '0':
                count2 += 1

        return min(count, count2)
