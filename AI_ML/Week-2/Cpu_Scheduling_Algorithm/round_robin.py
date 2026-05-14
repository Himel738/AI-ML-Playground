from collections import deque

def round_robin(df, time_quantum):

    n = len(df)

    burst_time = df["Burst Time"].tolist()
    arrival_time = df["Arrival Time"].tolist()

    remaining_burst_time = burst_time.copy()

    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n

    ready_queue = deque()

    current_time = 0
    completed = 0

    visited = [False] * n

    while completed < n:

        # Add arrived processes to queue
        for i in range(n):
            if arrival_time[i] <= current_time and not visited[i]:
                ready_queue.append(i)
                visited[i] = True

        # CPU idle
        if not ready_queue:
            current_time += 1
            continue

        process = ready_queue.popleft()

        execution_time = min(time_quantum,
                             remaining_burst_time[process])

        remaining_burst_time[process] -= execution_time
        current_time += execution_time

        # Add newly arrived processes during execution
        for i in range(n):
            if arrival_time[i] <= current_time and not visited[i]:
                ready_queue.append(i)
                visited[i] = True

        # If process unfinished, push back
        if remaining_burst_time[process] > 0:
            ready_queue.append(process)

        else:
            completion_time[process] = current_time
            completed += 1

    turnaround_time = [
        completion_time[i] - arrival_time[i]
        for i in range(n)
    ]

    waiting_time = [
        turnaround_time[i] - burst_time[i]
        for i in range(n)
    ]

    df["Completion Time"] = completion_time
    df["Waiting Time"] = waiting_time
    df["Turnaround Time"] = turnaround_time

    return df, current_time