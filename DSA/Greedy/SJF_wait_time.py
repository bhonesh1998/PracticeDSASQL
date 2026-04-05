jobs = [4, 3, 7, 1, 2]

jobs.sort()

n = len(jobs)
prefix_sums = [0] * n
prefix_sums[0] = jobs[0]

for i in range(1, n):
    prefix_sums[i] = prefix_sums[i-1] + jobs[i]

total_waiting_time = sum(prefix_sums[:-1])
avg_waiting_time = total_waiting_time / n

print(avg_waiting_time)