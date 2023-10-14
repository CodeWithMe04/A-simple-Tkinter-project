import tkinter as tk
from tkinter import messagebox


def add_task():
  task = task_entry.get()
  if task:
    task_list.insert(tk.END, task)
    task_entry.delete(0, tk.END)
  else:
    messagebox.showwarning("Warning", "You must enter a task.")


def remove_task():
  try:
    selected_task = task_list.curselection()[0]
    task_list.delete(selected_task)
  except IndexError:
    messagebox.showwarning("Warning", "You must select a task to remove.")


# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Task entry field
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Add and Remove buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
add_button.pack()
remove_button.pack()

# Task list
task_list = tk.Listbox(root, height=10, selectbackground="yellow")
task_list.pack()

# Main loop
root.mainloop()
