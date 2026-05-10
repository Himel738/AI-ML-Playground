def priority_scheduling_preemptive(df):
    remaining_burst_time = df["Burst Time"].tolist()
    arrival_time = df["Arrival Time"].tolist()
    priority = df["Priority"].tolist()
    waiting_time = [0] * len(df)
    completion_time = [0] * len(df)
    
    current_time = 0
    completed = 0
    
    while completed < len(df):
        # Find the process with highest priority that has arrived and has remaining burst time
        max_priority = -1
        next_process = -1
        
        for i in range(len(df)):
            if arrival_time[i] <= current_time and remaining_burst_time[i] > 0:
                if priority[i] > max_priority:
                    max_priority = priority[i]
                    next_process = i
        
        # If no process has arrived, move time to next arrival
        if next_process == -1:
            for i in range(len(df)):
                if remaining_burst_time[i] > 0:
                    current_time = arrival_time[i]
                    next_process = i
                    break
        
        # Execute 1 unit of the selected process
        remaining_burst_time[next_process] -= 1
        current_time += 1
        
        # If process is completed, record completion time
        if remaining_burst_time[next_process] == 0:
            completion_time[next_process] = current_time
            completed += 1
    
    # Calculate waiting time and turnaround time
    turnaround_time = [completion_time[i] - arrival_time[i] for i in range(len(df))]
    waiting_time = [turnaround_time[i] - df.iloc[i]["Burst Time"] for i in range(len(df))]
    
    df["Waiting Time"] = waiting_time
    df["Turnaround Time"] = turnaround_time
    
    return df, current_time
