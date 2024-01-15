from typing import List,Dict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        record = {}
        for match in matches:
            if match[0] not in record.keys():
                record[match[0]] = 0
            if match[1] not in record.keys():
                record[match[1]] = 1
            else:
                record[match[1]] +=1
        result = [[],[]]
        for k,v in record.items():
            if v == 0:
                result[0].append(k)
            elif v == 1:
                result[1].append(k)
        return [sorted(result[0]),sorted(result[1])]

if __name__ == '__main__':
    matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    print(Solution().findWinners(matches=matches))