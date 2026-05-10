import streamlit as st
import pandas as pd
from first_come_first_service import first_come_first_service
from shortest_job_first_non_premitive import shortest_job_first
from shortest_job_first_preemptive import shortest_job_first_preemptive
from round_robin import round_robin
from priority_scheduling_non_premitive import priority_scheduling_non_preemptive
from priority_scheduling_preemptive import priority_scheduling_preemptive
import shortest_job_first_non_premitive

with st.sidebar:
   algo = st.selectbox("Choose Scheduling Algorithm",
                       options=["First Come First Serve", "Shortest Job First(Non-Preemptive)","Shortest Job First(Preemptive)", "Round Robin","priority Scheduling(Non-Preemptive)","priority Scheduling(Preemptive)"],
                       index = None,
                       placeholder="Select an algorithm")
   number_of_processes = st.number_input("Number of Processes", min_value=1, step=1)
   process = []

   if algo:
      for i in range(int(number_of_processes)):
         st.markdown(f"**Process {i+1}**")
         col1, col2 = st.columns(2)
         with col1:
            arrival_time = st.number_input(f"Arrival Time for Process {i+1}", 
                                             min_value=0, 
                                             step=1,
                                             key=f"arrival_{i}")
         with col2:
            burst_time = st.number_input(f"Burst Time for Process {i+1}", 
                                             min_value=1, 
                                             step=1,
                                             key=f"burst_{i}")
         
         if "priority" in algo.lower():
            priority = st.number_input(f"Priority for Process {i+1}", 
                                         min_value=0, 
                                         step=1,
                                         key=f"priority_{i}")
            process.append((i+1, arrival_time, burst_time, priority))
         else:
            process.append((i+1, arrival_time, burst_time))
   if algo == "Round Robin":
      time_quantum = st.number_input("Time Quantum", min_value=1, step=1)
   button = st.button("Schedule",type = "primary")

st.title("CPU Scheduling Algorithms")
if button and not algo:
   st.warning("Please select a scheduling algorithm.")
if not algo:
    st.info("Please select a scheduling algorithm and input process details to see the scheduling results.")
if button:
    if "priority" in algo.lower():
        df = pd.DataFrame(process, columns=["Process", "Arrival Time", "Burst Time", "Priority"])
    else:
        df = pd.DataFrame(process, columns=["Process", "Arrival Time", "Burst Time"])
    st.subheader("Input Process Details")
    st.dataframe(df)
    st.subheader("Scheduling Results")
    if algo == "First Come First Serve":
        result,total_time = first_come_first_service(df)
        st.markdown(f"### First Come First Serve Scheduling Takes :red[{total_time} Unit Time] Based On Your Inputs:")
        st.dataframe(result)
    elif algo == "Shortest Job First(Non-Preemptive)":
        result,total_time = shortest_job_first(df)
        st.markdown(f"### Shortest Job First (Non-Preemptive) Scheduling Takes :red[{total_time} Unit Time] Based On Your Inputs:")
        st.dataframe(result)
    elif algo == "Shortest Job First(Preemptive)":
        result,total_time = shortest_job_first_preemptive(df)
        st.markdown(f"### Shortest Job First (Preemptive) Scheduling Takes :red[{total_time} Unit Time] Based On Your Inputs:")
        st.dataframe(result)
    elif algo == "Round Robin":
        result,total_time = round_robin(df,time_quantum)
        st.markdown(f"### Round Robin Scheduling Takes :red[{total_time} Unit Time] Based On Your Inputs:")
        st.dataframe(result)
    elif algo == "priority Scheduling(Non-Preemptive)":
        result,total_time = priority_scheduling_non_preemptive(df)
        st.markdown(f"### Priority Scheduling (Non-Preemptive) Takes :red[{total_time} Unit Time] Based On Your Inputs:")
        st.dataframe(result)
    elif algo == "priority Scheduling(Preemptive)":
        result,total_time = priority_scheduling_preemptive(df)
        st.markdown(f"### Priority Scheduling (Preemptive) Takes :red[{total_time} Unit Time] Based On Your Inputs:")
        st.dataframe(result)
        
   



             