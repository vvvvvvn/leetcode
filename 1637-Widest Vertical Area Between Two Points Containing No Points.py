from typing import List
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_elements = [point[0] for point in points]
        x_elements.sort()
        print(x_elements)
        max = 0
        for i, x in enumerate(x_elements):
            if i+1 < len(x_elements):
                max = x_elements[i+1] - x if x_elements[i+1] - x > max else max

        return max
if __name__ == '__main__':
    points = [[8,7],[9,9],[7,4],[9,7]]
    sol = Solution()
    print(sol.maxWidthOfVerticalArea(points))