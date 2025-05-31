import heapq
from collections import defaultdict
from typing import List
# Problem name: Leetcode 3387. Maximise amount after two days of conversions
# approach: Run dijkstra on the first graph, this gives amount I can get for each currency conversion 
# from initialCurrency considering initialCurrency as start, then for each currency found in this dijkstra
# take it as the start node and run dijkstra, this gives the max amount for initialCurrency I can get starting 
# with a different currency encountered on day1, keep track of the max amount that I can get from each conversion back
# to initial currncy. In the end return the max conversion amount possible.
class Solution:
    def dijkstra(self, g, start):
        max_heap = []
        prices = defaultdict(float)
        prices[start] = 1
        heapq.heappush(max_heap, (-1, start))
        while max_heap:
            price, node = heapq.heappop(max_heap)
            price *= -1
            for neighbor, cur_price in g[node]:
                new_price = cur_price * price
                if new_price > prices[neighbor]:
                    prices[neighbor] = new_price
                    heapq.heappush(max_heap, (-1*new_price, neighbor))
        return prices

    def create_graph(self, pairs, rates):
        n = len(rates)
        g = defaultdict(list)
        for i in range(n):
            start_cur, target_cur, rate = pairs[i][0], pairs[i][1], rates[i]
            g[start_cur].append((target_cur, rate))
            g[target_cur].append((start_cur, 1/rate))
        return g

    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        g1 = self.create_graph(pairs1, rates1)
        g2 = self.create_graph(pairs2, rates2)
        prices_d1 = self.dijkstra(g1, initialCurrency)
        max_price = 0
        for currency in prices_d1.keys():
            price = prices_d1[currency] * self.dijkstra(g2, currency)[initialCurrency]
            max_price = max(max_price, price)
        return max_price