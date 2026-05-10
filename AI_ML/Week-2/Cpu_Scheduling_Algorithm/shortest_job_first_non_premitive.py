def shortest_job_first(df):
    df = df.sort_values(by="Arrival Time").reset_index(drop=True)
    waiting_time = [0] * len(df)
    turnaround_time = [0] * len(df)
    current_time = 0
    completed = [False] * len(df)
    
    for _ in range(len(df)):
        # Find the next process to execute (shortest burst time among arrived processes)
        next_process = -1
        min_burst = float('inf')
        
        for i in range(len(df)):
            if not completed[i] and df.iloc[i]["Arrival Time"] <= current_time:
                if df.iloc[i]["Burst Time"] < min_burst:
                    min_burst = df.iloc[i]["Burst Time"]
                    next_process = i
        
        # If no process has arrived, move time forward to next arrival
        if next_process == -1:
            for i in range(len(df)):
                if not completed[i]:
                    current_time = df.iloc[i]["Arrival Time"]
                    next_process = i
                    break
        
        # Execute the selected process
        arrival_time = df.iloc[next_process]["Arrival Time"]
        burst_time = df.iloc[next_process]["Burst Time"]
        
        waiting_time[next_process] = current_time - arrival_time
        current_time += burst_time
        turnaround_time[next_process] = current_time - arrival_time
        completed[next_process] = True
    
    df["Waiting Time"] = waiting_time
    df["Turnaround Time"] = turnaround_time
    
    return df, current_time