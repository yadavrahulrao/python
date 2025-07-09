def optimal_bst(keys, prob):
    n = len(keys)
    cost = [[0 for _ in range(n)] for _ in range(n)]
    root = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        cost[i][i] = prob[i]
        root[i][i] = i
    for length in range(2, n + 1):  
        for i in range(n - length + 1):
            j = i + length - 1  
            cost[i][j] = float('inf')
            for r in range(i, j + 1):
                left_cost = cost[i][r - 1] if r > i else 0
                right_cost = cost[r + 1][j] if r < j else 0
                total_cost = left_cost + right_cost + sum(prob[i:j + 1])
                if total_cost < cost[i][j]:
                    cost[i][j] = total_cost
                    root[i][j] = r
    print("\nRoot Matrix:")
    for row in root:
        print(row)
keys = [10, 12, 20, 30]
prob = [0.1, 0.4, 0.2, 0.3]
optimal_bst(keys, prob)
