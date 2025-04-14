class Job:
    def __init__(self, id, deadline, profit):
        self.id = id      
        self.deadline = deadline  
        self.profit = profit    
def job_sequencing(jobs, n):
    jobs.sort(key=lambda x: x.profit, reverse=True)
    time_slots = [-1] * n  
    job_sequence = [None] * n  
    total_profit = 0  
    for job in jobs:
        for t in range(min(n, job.deadline) - 1, -1, -1):
            if time_slots[t] == -1:  
                time_slots[t] = job.id
                job_sequence[t] = job
                total_profit += job.profit
                break  
    scheduled_jobs = [job.id for job in job_sequence if job is not None]
    return scheduled_jobs, total_profit
jobs = [
    Job('J1', 4, 20),
    Job('J2', 1, 10),
    Job('J3', 1, 40),
    Job('J4', 1, 30),
]
n = len(jobs)
scheduled_jobs, total_profit = job_sequencing(jobs, n)
print("Job sequence to maximize profit:", scheduled_jobs)
print("Total profit:", total_profit)
