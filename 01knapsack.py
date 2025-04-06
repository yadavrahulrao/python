def knap(weight,capacity,value):
  n = len(weight)
  dp = [[0 for _ in range (capacity +1)]for _ in range(n+1)]
  for i in range(n+1):
    for w in range(capacity+1):
      if i==0 or w == 0:
        dp[i][w] = 0
      elif weight[i-1]<= w:
        dp[i][w] = max(value[i-1] + dp[i-1][w - weight[i-1]],dp[i-1][w])
      else :
        dp[i][w] = dp[i-1][w]
  return dp[n][capacity]

weight = [2,3,4,5]
value = [3,4,5,6]
capacity = 5
max_value = knap(weight, capacity , value)
print("Maximum value is obtained :",max_value)