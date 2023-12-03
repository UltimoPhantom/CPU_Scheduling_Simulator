class RoundRobin:

    def processData(self, tasks, time_quantum):
        process_data = []

        for task in tasks:
            temp = [task[0], task[1], task[2], 0, task[2]]  # [name, arrival, burst, status, remaining burst]
            process_data.append(temp)

        process_data.sort(key=lambda x: x[1])  # Sort processes according to Arrival Time

        result = self.schedulingProcess(process_data, time_quantum)
        return result

    def schedulingProcess(self, process_data, time_quantum):
        start_time = []
        exit_time = []
        sequence_of_process = []
        s_time = 0

        while any(process[3] == 0 for process in process_data):
            for j in range(len(process_data)):
                if process_data[j][3] == 0 and process_data[j][1] <= s_time:
                    start_time.append(s_time)

                    if process_data[j][4] > time_quantum:
                        s_time += time_quantum
                        exit_time.append(s_time)
                        sequence_of_process.append(process_data[j][0])
                        process_data[j][4] -= time_quantum
                    else:
                        s_time += process_data[j][4]
                        exit_time.append(s_time)
                        sequence_of_process.append(process_data[j][0])
                        process_data[j][4] = 0
                        process_data[j][3] = 1
                        process_data[j].append(s_time)  # Fix: Append completion time here

            if all(process[3] == 1 for process in process_data):
                break

            if process_data[0][1] > s_time:
                start_time.append(s_time)
                s_time = process_data[0][1]
                exit_time.append(s_time)
                sequence_of_process.append(-1)

        t_time = self.calculateTurnaroundTime(process_data)
        w_time = self.calculateWaitingTime(process_data)
        return sequence_of_process, t_time, w_time

    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][5] - process_data[i][1]
            total_turnaround_time += turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        return average_turnaround_time

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][2]
            total_waiting_time += waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        return average_waiting_time

    def printData(self, process_data, average_turnaround_time, average_waiting_time, sequence_of_process):
        process_data.sort(key=lambda x: x[0])

        print("Process_ID  Arrival_Time  Rem_Burst_Time   Completed  Orig_Burst_Time Completion_Time  Turnaround_Time  Waiting_Time")
        for i in range(len(process_data)):
            for j in range(len(process_data[i])):
                print(process_data[i][j], end="               ")
            print()

        print(f'Average Turnaround Time: {average_turnaround_time}')
        print(f'Average Waiting Time: {average_waiting_time}')
        print(f'Sequence of Process: {sequence_of_process}')


tasks = [["P1", 0, 5], ["P2", 1, 4], ["P3", 2, 2], ["P4", 3, 1]]
time_quantum = 2
round_robin = RoundRobin()
print(round_robin.processData(tasks, time_quantum))