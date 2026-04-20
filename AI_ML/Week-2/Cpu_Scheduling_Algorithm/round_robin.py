def round_robin(df,time_quantum):
    remaining_burst_time = df["Burst Time"].tolist()
    arrival_time = df["Arrival Time"].tolist()
    waiting_time = [0] * len(df)

    current_time = 0

    while True:
        done = True

        for i in range(len(df)):
            if remaining_burst_time[i] > 0:
                done = False
                if arrival_time [i] <= current_time:
                    if remaining_burst_time[i] > time_quantum:
                        current_time += time_quantum
                        remaining_burst_time[i] -= time_quantum
                    else:
                        current_time += remaining_burst_time[i]
                        waiting_time[i] = current_time - arrival_time[i] - df.iloc[i]["Burst Time"] # Waiting Time = Current Time - Arrival Time - Burst Time
                        remaining_burst_time[i] = 0
        if done:
            break
    turnaround_time = [waiting_time[i] + df.iloc[i]["Burst Time"] for i in range(len(df))] # Turnaround Time = Waiting Time + Burst Time
    df["Waiting Time"] = waiting_time
    df["Turnaround Time"] = turnaround_time

    return df,current_time

