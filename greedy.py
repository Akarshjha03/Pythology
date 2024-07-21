from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        candies=[1]*len(ratings)
        for L in range(1,len(ratings)):
            if (ratings[L]>ratings[L-1]):
                candies[L]=candies[L-1]+1
        for R in range(len(ratings)-2,-1,-1):
            if ratings[R]>ratings[R+1]:
                r=candies[R+1]+1
                if r>candies[R]:
                    candies[R]=r
        return sum(candies)