import heapq
class Item:
    def __init__(self, weight, profit):
        self.weight = weight
        self.profit = profit
        self.ratio = profit / weight
class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound
    def __lt__(self, other):
        return self.bound > other.bound
def bound(node, n, W, items):
    if node.weight >= W:
        return 0
    profit_bound = node.profit
    j = node.level + 1
    totweight = node.weight
    while j < n and totweight + items[j].weight <= W:
        totweight += items[j].weight
        profit_bound += items[j].profit
        j += 1
    if j < n:
        profit_bound += (W - totweight) * items[j].ratio
    return profit_bound
def knapsack_branch_and_bound(weights, profits, W):
    n = len(weights)
    items = [Item(weights[i], profits[i]) for i in range(n)]
    items.sort(key=lambda x: x.ratio, reverse=True)
    Q = []
    root = Node(level=-1, profit=0, weight=0, bound=0)
    root.bound = bound(root, n, W, items)
    max_profit = 0
    heapq.heappush(Q, root)
    while Q:
        node = heapq.heappop(Q)
        if node.bound > max_profit and node.level < n - 1:
            u = Node(level=node.level + 1, profit=0, weight=0, bound=0)
            u.weight = node.weight + items[u.level].weight
            u.profit = node.profit + items[u.level].profit
            if u.weight <= W and u.profit > max_profit:
                max_profit = u.profit
            u.bound = bound(u, n, W, items)
            if u.bound > max_profit:
                heapq.heappush(Q, u)
            u2 = Node(level=node.level + 1, profit=node.profit, weight=node.weight, bound=0)
            u2.bound = bound(u2, n, W, items)
            if u2.bound > max_profit:
                heapq.heappush(Q, u2)
    return max_profit
if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    profits = [3, 4, 5, 6]
    W = 5
    max_profit = knapsack_branch_and_bound(weights, profits, W)
    print("Maximum Profit:", max_profit)
