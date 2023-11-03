import tkinter as tk
from tkinter import ttk

def add_task():
    task_name = task_name_entry.get()
    task_description = task_description_text.get("1.0", tk.END)
    task_details = f"Task: {task_name}\nDescription: {task_description}"
    tasks_listbox.insert(tk.END, task_details)

def delete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)

def save_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        task_name = task_name_entry.get()
        task_description = task_description_text.get("1.0", tk.END)
        task_details = f"Task: {task_name}\nDescription: {task_description}"
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(selected_task_index, task_details)

root = tk.Tk()
root.title("To-Do List")

tasks_frame = ttk.Frame(root)
tasks_frame.pack(fill=tk.BOTH, expand=True)


tasks_listbox = tk.Listbox(tasks_frame)
tasks_listbox.pack(fill=tk.BOTH, expand=True)

add_task_button = ttk.Button(tasks_frame, text="Add Task", command=add_task)
add_task_button.pack()

delete_task_button = ttk.Button(tasks_frame, text="Delete Task", command=delete_task)
delete_task_button.pack()

task_details_frame = ttk.Frame(root)
task_details_frame.pack(fill=tk.BOTH, expand=True)


task_name_label = ttk.Label(task_details_frame, text="Task Name")
task_name_label.pack()

task_name_entry = ttk.Entry(task_details_frame)
task_name_entry.pack()

task_description_label = ttk.Label(task_details_frame, text="Task Description")
task_description_label.pack()

task_description_text = tk.Text(task_details_frame)
task_description_text.pack()

save_task_button = ttk.Button(task_details_frame, text="Save Task", command=save_task)
save_task_button.pack()

root.mainloop()
