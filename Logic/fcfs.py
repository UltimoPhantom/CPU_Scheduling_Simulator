class Fcfs:
    def processData(self, Tasks):
        # Tasks: list of tuples representing tasks
        # Each tuple: (process name, arrival time, burst time)

        # Sort tasks according to their arrival time
        Tasks = sorted(Tasks, key=lambda x: x[1])

        # Initialize variables
        process_names = []
        arrival_times = []
        burst_times = []
        sequence = []
        time = 0
        task_count = len(Tasks)
        indx = 0

        while indx < len(Tasks):
            # Check if current task is ready
            if Tasks[indx][2] > 0 and time >= Tasks[indx][1]:
                # Execute the current task
                sequence.append(Tasks[indx][0])
                Tasks[indx][2] -= 1
                time += 1
                print(Tasks[indx][0])
            elif time < Tasks[indx][1]:
                time += 1
                sequence.append(-1)
            else:
                indx += 1
                
            # Idle time if no task is ready
            # if Tasks[indx][2] == 0:
            #     sequence.append(-1)
            #     time += 1
            #     task_count -= 1

        return sequence, time




ff = Fcfs()
task = list([('Task1', 2, 1, 2, -1, -1), ('Task2', 4, 1, 1, -1, -1), ('Task3', 7, 2, 3, -1, -1)])
ans = []
for i in task:
    ans.append(list(i))

print(ff.processData(ans)) 

