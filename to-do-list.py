import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        # Colors
        self.bg_color = "#F0F0F0"
        self.btn_bg_color = "#6AB6F8"
        self.btn_fg_color = "#FFFFFF"
        self.task_color = "#333333"

        # Fonts
        self.heading_font = ("Arial", 20, "bold")
        self.task_font = ("Arial", 14)
        
        # Main Frame
        self.main_frame = tk.Frame(master, bg=self.bg_color)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Task Frame
        self.task_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.task_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Tasks Label
        self.tasks_label = tk.Label(self.task_frame, text="Tasks", font=self.heading_font, bg=self.bg_color, fg=self.task_color)
        self.tasks_label.pack(anchor=tk.W)

        # Task List
        self.task_list = tk.Listbox(self.task_frame, font=self.task_font, bg=self.bg_color, fg=self.task_color)
        self.task_list.pack(fill=tk.BOTH, expand=True)

        # Options Frame
        self.options_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.options_frame.pack(side=tk.RIGHT, fill=tk.Y)

        # Buttons
        self.add_button = self.create_button("Add Task", self.add_task)
        self.delete_button = self.create_button("Delete Task", self.delete_task)
        self.delete_all_button = self.create_button("Delete All", self.delete_all_tasks)
        self.exit_button = self.create_button("Exit", self.exit_app)

    def create_button(self, text, command):
        button = tk.Button(self.options_frame, text=text, bg=self.btn_bg_color, fg=self.btn_fg_color, font=self.task_font, command=command)
        button.pack(fill=tk.X, padx=10, pady=5)
        return button

    def add_task(self):
        task_text = simpledialog.askstring("Add Task", "Enter Task:")
        if task_text:
            self.task_list.insert(tk.END, task_text)

    def delete_task(self):
        if self.task_list.curselection():
            confirm = messagebox.askyesno("Delete Task", "Are you sure you want to delete the selected task?")
            if confirm:
                selected_index = self.task_list.curselection()[0]
                self.task_list.delete(selected_index)
        else:
            messagebox.showinfo("No Task Selected", "Please select a task to delete.")

    def delete_all_tasks(self):
        if self.task_list.size() > 0:
            confirm = messagebox.askyesno("Delete All Tasks", "Are you sure you want to delete all tasks?")
            if confirm:
                self.task_list.delete(0, tk.END)
        else:
            messagebox.showinfo("No Tasks", "There are no tasks to delete.")

    def exit_app(self):
        confirm = messagebox.askyesno("Exit", "Are you sure you want to exit the application?")
        if confirm:
            self.master.destroy()

root = tk.Tk()
app = TodoApp(root)
root.mainloop()
