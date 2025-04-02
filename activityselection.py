def activitySelection(start, finish, n):
    activities = [(start[i], finish[i]) for i in range(n)]
    activities.sort(key=lambda x: x[1])
    selected_activities = []
    last_finish_time = -1  
    for activity in activities:
        if activity[0] >= last_finish_time:
            selected_activities.append(activity)
            last_finish_time = activity[1]  
    return selected_activities
start_times = [1, 3, 0, 5, 8, 5]
finish_times = [2, 4, 6, 7, 9, 9]
n = len(start_times)
selected = activitySelection(start_times, finish_times, n)
print("Selected activities (start, finish):")
for activity in selected:
    print(f"Start: {activity[0]}, Finish: {activity[1]}")
