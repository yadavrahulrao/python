def canCompleteCircuit(gas, cost):
    total_gas = 0
    total_cost = 0
    current_tank = 0
    start_index = 0
    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]
        current_tank += gas[i] - cost[i]
        if current_tank < 0:
            start_index = i + 1
            current_tank = 0  
    if total_gas >= total_cost:
        return start_index
    else:
        return -1
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
result = canCompleteCircuit(gas, cost)
print(result)  
