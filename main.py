# from UI.first_window import InputWindow
# from UI.second_window import InputWindow2
# from Data.insertion import insert_values
# from Logic.priority_temp import Priority
# from UI.Priority_Output import Priority_Output

# input_window = InputWindow()
# ans = input_window.get_input_values()

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
from Data.insertion import insert_values
from Logic.priority_temp import Priority
from UI.Priority_Output import Priority_Output

input_window = InputWindow()
ans = input_window.get_input_values()

input_window2 = InputWindow2(ans)
Tasks, tq = input_window2.get_input_values()

# insert_values(Tasks, tq)
print(Tasks)

# ... (previous code)

if tq == -1:
    priority_instance = Priority()
    res = priority_instance.processData(Tasks)
    print("*** ", res, " ***")
    Tasks = list(Tasks)
    newTask = []
    for it in Tasks:
        newTask.append(list(it))
    priority_instance_output = Priority_Output(newTask, res)
    priority_instance_output.start_updates()
    priority_instance_output.mainloop()
