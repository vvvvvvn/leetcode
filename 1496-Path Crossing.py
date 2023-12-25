import copy


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        point = [0, 0]
        history = [[0, 0]]
        for p in path:
            temp = copy.deepcopy(history[-1])
            print(f'current (x,y):{temp}')
            print(f'current history: {history}')
            # temp = copy.deepcopy()
            if p == 'N':
                temp[1] += 1
            elif p == 'S':
                temp[1] -= 1
            elif p == 'E':
                temp[0] += 1
            else:
                temp[0] -= 1
            print(f'after (x,y):{temp}')
            print(f'current history: {history}')
            if temp in history:
                print(123)
                print(point)
                print(history)
                return True
            else:
                print(456)
                print(temp)
                history.append(temp)
            print(f'after history: {history}')
            print('-'*10)
        return False


if __name__ == '__main__':
    path = "NNSWWEWSSESSWENNW"
    a = [[0, 0], [0, 1]]
    # print([1, 1] in a)
    print(Solution().isPathCrossing(path))
