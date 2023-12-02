class Fcfs:
    def processData(self, Tasks):
        # Tasks: list of tuples representing tasks

        # Sort tasks according to their arrival time
        Tasks = sorted(Tasks, key=lambda x: x[1])

        # Initialize variables
        sequence = []
        waiting_time = []
        turnAround_time = []
        time = 0
        task_count = len(Tasks)
        indx = 0
        firstFlag = True
        while indx < len(Tasks):
            # Check if current task is ready
            if Tasks[indx][2] > 0 and time >= Tasks[indx][1]:
                # Execute the current task
                sequence.append(Tasks[indx][0])
                Tasks[indx][2] -= 1
                time += 1
                if firstFlag:
                    firstFlag = False
                    waiting_time.append(time - Tasks[indx][1] - 1)
                    turnAround_time.append(Tasks[indx][2] + waiting_time[-1] + 1)
            elif time < Tasks[indx][1]:
                time += 1
                sequence.append(-1)
            else:
                indx += 1
                firstFlag = True
                
        print("*** Waiting Time ***")
        print(waiting_time)
        print("****")
        
        print("*** Turn Around Time ***")
        print(turnAround_time)
        print("****")
        return sequence, time




ff = Fcfs()
task = list([('Task1', 2, 12, 2, -1, -1), ('Task2', 6, 2, 1, -1, -1), ('Task3', 10, 1, 3, -1, -1)])
ans = []
for i in task:
    ans.append(list(i))

print(ff.processData(ans)) 

