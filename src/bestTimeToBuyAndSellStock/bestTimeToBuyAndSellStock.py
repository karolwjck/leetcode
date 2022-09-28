from ast import List

class Solution:
    def maxProfit(self, prices : List[int]) -> int:
        leftPointer, rightPointer = 0, 1
        maxProfit = 0
        
        while rightPointer < len(prices):
            if prices[leftPointer] < prices[rightPointer]:
                profit = prices[rightPointer] - prices[leftPointer]
                maxProfit = max(maxProfit, profit)
            else:
                leftPointer = rightPointer
            rightPointer += 1
            
        return maxProfit