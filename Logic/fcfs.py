class Fcfs:
    def processData(Tasks):
        #Tasks [ name, arrival, burst, priority, status, burst]
        processes = []
        waiting_time = [0] * n
        total_waiting_time = 0
        total_turnaround_time = 0
        burst_time = [0] * n
        turnaround_time = [0] * n
        
        n = len(processes)
        for i in len(Tasks):
            processes[i] = Tasks[i][0]
            
            
        # Calculate turnaround time and waiting time
        for i in range(n):
            if i == 0:
                turnaround_time[i] = burst_time[i]
            else:
                turnaround_time[i] = turnaround_time[i - 1] + burst_time[i]
            
            waiting_time[i] = turnaround_time[i] - burst_time[i]
            total_waiting_time += waiting_time[i]
            total_turnaround_time += turnaround_time[i]

        # Calculate average waiting time and average turnaround time
        average_waiting_time = total_waiting_time / n
        average_turnaround_time = total_turnaround_time / n

        print("Average Waiting Time:", average_waiting_time)
        print("Average Turnaround Time:", average_turnaround_time)


