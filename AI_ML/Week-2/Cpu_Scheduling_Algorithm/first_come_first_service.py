def first_come_first_service(df):
  df = df.sort_values(by = "Arrival Time").reset_index(drop = True)
  waiting_time = []
  turnaround_time = []
  current_time = 0

  for i in range(len(df)):
    arrival_time = df.iloc[i]["Arrival Time"]
    burst_time = df.iloc[i]["Burst Time"]

    if current_time < arrival_time:
      current_time = arrival_time
    waiting = current_time - arrival_time
    turnaround = waiting + burst_time

    waiting_time.append(waiting)
    turnaround_time.append(turnaround)

    current_time += burst_time

  df["Waiting Time"] = waiting_time
  df["Turnaround Time"] = turnaround_time

  return df,current_time


    