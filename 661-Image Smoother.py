from typing import List
import math

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m,n = len(img), len(img[0])
        result = [[0 for _ in range(n)] for _ in range(m)]
        for i,row in enumerate(img):
            for j, cell in enumerate(row):
                print(f'cell: {cell}')
                surrounding_sum = 0
                divisor = 0
                if i-1 >= 0:
                    print('i-1')
                    if j-1>=0:
                        print('j-1')
                        divisor +=1
                        surrounding_sum = img[i-1][j-1]
                    if j+1 < n:
                        print('j+1')
                        surrounding_sum += img[i-1][j+1]
                        divisor +=1
                    divisor +=1
                    surrounding_sum += img[i-1][j]
                if j-1 >= 0:
                    print('j-1')
                    if i+1 < m:
                        print('i+1')
                        divisor +=1
                        surrounding_sum += img[i+1][j-1]
                    divisor +=1
                    surrounding_sum += img[i][j-1]
                if i+1 < m:
                    print('i+1')
                    if j+1 < n:
                        print('j+1')
                        divisor +=1
                        surrounding_sum += img[i+1][j+1]
                    divisor +=1
                    surrounding_sum += img[i+1][j]
                if j+1 < n:
                    print('j+1')
                    divisor +=1
                    surrounding_sum += img[i][j+1]
                divisor +=1
                surrounding_sum += cell

                result[i][j] = math.floor(surrounding_sum/divisor)
                print('_'*20)
        return result
        

if __name__ == '__main__':
    img = [[100,200,100],[200,50,200],[100,200,100]]
    sol = Solution()
    print(sol.imageSmoother(img))