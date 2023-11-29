from UI.first_window import InputWindow
from UI.second_window import InputWindow2
from Data.insertion import insert_values
from Logic.priority_temp import Priority

input_window = InputWindow()
ans = input_window.get_input_values()
print(ans)

input_window2 = InputWindow2(ans)
Tasks,tq = input_window2.get_input_values()

# insert_values(Tasks,tq)
print(Tasks)

if tq == -1:
    priority_instance = Priority()
    priority_instance.processData(Tasks)

