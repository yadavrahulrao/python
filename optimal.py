def optimal_bst(keys, prob):
    n = len(keys)
    
    # cost[i][j] will store the minimum cost for keys[i..j]
    cost = [[0 for _ in range(n)] for _ in range(n)]
    
    # root[i][j] will store the index of the root of the optimal BST for keys[i..j]
    root = [[0 for _ in range(n)] for _ in range(n)]
    
    # Base case: single keys
    for i in range(n):
        cost[i][i] = prob[i]
        root[i][i] = i
    
    # Build the cost table using dynamic programming
    for length in range(2, n + 1):  # length of the subproblem
        for i in range(n - length + 1):
            j = i + length - 1  # range of the subproblem [i..j]
            cost[i][j] = float('inf')
            
            # Try every key in the range [i..j] as the root
            for r in range(i, j + 1):
                # Cost of left and right subtrees plus the sum of probabilities of all keys in the range
                left_cost = cost[i][r - 1] if r > i else 0
                right_cost = cost[r + 1][j] if r < j else 0
                total_cost = left_cost + right_cost + sum(prob[i:j + 1])
                
                # Update cost and root if we found a smaller cost
                if total_cost < cost[i][j]:
                    cost[i][j] = total_cost
                    root[i][j] = r
    
    # Print the cost matrix
    # print("Cost Matrix:")
    # for row in cost:
    #     print(row)
    
    # Print the root matrix
    print("\nRoot Matrix:")
    for row in root:
        print(row)

# Example usage
keys = [10, 12, 20, 30]
prob = [0.1, 0.4, 0.2, 0.3]

optimal_bst(keys, prob)
