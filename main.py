# from UI.first_window import InputWindow
# from UI.second_window import InputWindow2
# from Data.insertion import insert_values
# from Logic.priority_temp import Priority
# from UI.Priority_Output import Priority_Output

# input_window = InputWindow()
# ans = input_window.get_input_values()``

# input_window2 = InputWindow2(ans)
# Tasks,tq = input_window2.get_input_values()

# # insert_values(Tasks,tq)
# print(Tasks)

# if tq == -1:
#     priority_instance = Priority()
#     res = priority_instance.processData(Tasks)
#     print("*** ", res, " ***")
#     Tasks = list(Tasks)
#     newTask = []
#     for it in Tasks:
#         newTask.append(list(it))
#     priority_instance_output = Priority_Output(newTask, res)
#     priority_instance_output.mainloop()


from UI.first_window import InputWindow
from UI.second_window import InputWindow2
from UI.Priority_Output import Priority_Output
from UI.fcfs_window import FCFS_Output
from Data.insertion import insert_values
from Logic.priority_prem import Priority
from Logic.fcfs import Fcfs
from Logic.round_robin import RoundRobin

input_window = InputWindow()
ans = input_window.get_input_values()
print("$$   ",ans)
input_window2 = InputWindow2(ans)
Tasks, tq = input_window2.get_input_values()

# insert_values(Tasks, tq)
print(Tasks)

if ans['algo'] == "Priority":
    priority_instance = Priority()
    res = priority_instance.processData(Tasks)
    Tasks = list(Tasks)
    newTask = []
    for it in Tasks:
        newTask.append(list(it))
    priority_instance_output = Priority_Output(newTask, res)
    # priority_instance_output.start_updates()  # Start updates in Priority_Output
    priority_instance_output.mainloop()

elif ans['algo'] == 'FCFS':
    Fcfs_instance = Fcfs()
    res = Fcfs_instance.processData(Tasks)
    print("RES RES  ",res)
    print(Tasks, res)
    fcfs_instance_output = FCFS_Output(Tasks, res)
    fcfs_instance_output.mainloop()

elif ans['algo'] == 'Round Robin':
    rr_instance = RoundRobin()
    res = rr_instance.processData(Tasks, int(tq))
    print(res)