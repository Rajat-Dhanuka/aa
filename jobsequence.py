#implement the greedy algorithm to solve the problem of the Job Sequencing with deadlines
def job_sequencing_with_deadlines(jobs):
    # Sort jobs based on their profits in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Find the maximum deadline among all jobs
    max_deadline = max(jobs, key=lambda x: x[1])[1]

    # Initialize the schedule with slots up to the maximum deadline
    schedule = [None] * (max_deadline + 1)

    total_profit = 0
    for job in jobs:
        deadline = job[1]
        # Find an available slot before the deadline
        while deadline > 0 and schedule[deadline] is not None:
            deadline -= 1
        if deadline > 0:
            schedule[deadline] = job[0]  # Assign the job to the slot
            total_profit += job[2]  # Add the job's profit to total profit

    return schedule, total_profit


# Example usage:
jobs_list = [('J1', 2, 40), ('J2', 1, 35), ('J3', 3, 30), ('J4', 1, 25), ('J5', 3, 20)]
schedule_result, total_profit_result = job_sequencing_with_deadlines(jobs_list)
print("Job Schedule:", schedule_result)
print("Total Profit:", total_profit_result)