import tkinter as tk
from tkinter import messagebox


class HabitTracker:

    def __init__(self, root):

        self.root = root
        self.root.title("Habit Tracker")
        self.root.geometry("450x550")
        self.root.resizable(True, True)
        self.root.state("zoomed")

        # List to store habits
        self.habits = []

        # Title
        title = tk.Label(root, text="My Habit Tracker", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        # Habit Entry
        tk.Label(root, text="Enter Habit:").pack()
        self.habit_entry = tk.Entry(root, width=35)
        self.habit_entry.pack(pady=5)

        # Note Entry
        tk.Label(root, text="Enter Note:").pack()
        self.note_entry = tk.Entry(root, width=35)
        self.note_entry.pack(pady=5)

        # Buttons
        tk.Button(root, text="Add Habit", width=18, command=self.add_habit).pack(pady=3)
        tk.Button(root, text="Mark as Done", width=18, command=self.mark_done).pack(pady=3)
        tk.Button(root, text="Delete Habit", width=18, command=self.delete_habit).pack(pady=3)

        # Listbox
        self.listbox = tk.Listbox(root, width=55, height=14)
        self.listbox.pack(pady=10)

        # Save Button
        tk.Button(root, text="Save Habits", width=18, command=self.save_habits).pack(pady=5)

        # Load saved data
        # self.load_habits()

    # Add Habit
    def add_habit(self):

        habit = self.habit_entry.get()
        note = self.note_entry.get()

        if habit == "":
            messagebox.showwarning("Warning", "Please enter a habit!")
            return

        if note == "":
            note = "No Note"

        habit_text = f"{habit} | Streak: 0 | Note: {note}"

        self.listbox.insert(tk.END, habit_text)

        # Clear boxes
        self.habit_entry.delete(0, tk.END)
        self.note_entry.delete(0, tk.END)

    # Mark Done → Increase Streak
    def mark_done(self):

        try:
            index = self.listbox.curselection()[0]
            text = self.listbox.get(index)

            parts = text.split("|")

            habit = parts[0].strip()
            streak_part = parts[1].strip()
            note_part = parts[2].strip()

            streak = int(streak_part.split(":")[1].strip())
            streak += 1

            new_text = f"{habit} | Streak: {streak} | {note_part}"

            self.listbox.delete(index)
            self.listbox.insert(index, new_text)

        except:
            messagebox.showwarning("Warning", "Please select a habit!")

    # Delete Habit
    def delete_habit(self):

        try:
            index = self.listbox.curselection()[0]
            self.listbox.delete(index)

        except:
            messagebox.showwarning("Warning", "Please select a habit!")

    # Save to File
    def save_habits(self):

        habits = self.listbox.get(0, tk.END)

        with open("habits.txt", "w") as file:
            for h in habits:
                file.write(h + "\n")

        messagebox.showinfo("Saved", "Habits saved successfully!")

    # Load From File
    def load_habits(self):

        try:
            with open("habits.txt", "r") as file:
                habits = file.readlines()

            for h in habits:
                self.listbox.insert(tk.END, h.strip())

        except:
            pass


# Main Program
root = tk.Tk()
app = HabitTracker(root)
root.mainloop()
