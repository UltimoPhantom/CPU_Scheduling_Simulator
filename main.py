from UI.first_window import InputWindow
from UI.second_window import InputWindow2

input_window = InputWindow()
ans = input_window.get_input_values()
print(ans)

input_window2 = InputWindow2(ans)
Tasks = input_window2.get_input_values()
print(Tasks)

# create_second_window(ans)