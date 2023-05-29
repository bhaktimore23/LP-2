def job_scheduling(jobs):
    # Sort the jobs by profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Find the maximum deadline among all jobs
    max_deadline = max(jobs, key=lambda x: x[1])[1]

    # Initialize the schedule and profit
    schedule = [-1] * max_deadline
    total_profit = 0

    # Iterate over the jobs
    for job in jobs:
        deadline = job[1]
        
        # Find the latest available slot before the deadline
        while deadline > 0:
            if schedule[deadline - 1] == -1:
                schedule[deadline - 1] = job[0]
                total_profit += job[2]
                break
            deadline -= 1

    return schedule, total_profit


# Example usage:
jobs = [(1, 2, 100), (2, 1, 19), (3, 2, 27), (4, 1, 25), (5, 3, 15)]

schedule, profit = job_scheduling(jobs)
print("Job Schedule:", schedule)
print("Total Profit:", profit)
