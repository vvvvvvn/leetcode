from typing import List

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        sorted_prices = sorted(prices)
        print(sorted_prices)
        if sorted_prices[0] + sorted_prices[1] > money:
            return money
        return money - sorted_prices[0] - sorted_prices[1]

if __name__ == '__main__':
    prices = [1,2,2]
    money = 3
    sol = Solution()
    print(sol.buyChoco(prices,money))