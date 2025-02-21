import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

# Database connection and table creation
conn = sqlite3.connect('habit_tracker.db')
c = conn.cursor()
c.execute('''
          CREATE TABLE IF NOT EXISTS habits
          (id INTEGER PRIMARY KEY AUTOINCREMENT, 
          habit_name TEXT NOT NULL, 
          date TEXT NOT NULL)
          ''')
conn.commit()

class HabitTracker:
    def _init_(self, root):
        self.root = root
        self.root.title("Habit Tracker")
        self.root.geometry("400x400")

        # Labels and Entries
        self.label = tk.Label(root, text="Enter your habit:")
        self.label.pack(pady=10)

        self.habit_entry = tk.Entry(root, width=40)
        self.habit_entry.pack(pady=10)

        # Buttons
        self.add_btn = tk.Button(root, text="Add Habit", command=self.add_habit)
        self.add_btn.pack(pady=10)

        self.view_btn = tk.Button(root, text="View Habits", command=self.view_habits)
        self.view_btn.pack(pady=10)

    def add_habit(self):
        habit_name = self.habit_entry.get()
        if habit_name:
            date = datetime.now().strftime("%Y-%m-%d")
            c.execute("INSERT INTO habits (habit_name, date) VALUES (?, ?)", (habit_name, date))
            conn.commit()
            messagebox.showinfo("Success", "Habit added successfully!")
            self.habit_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a habit.")

    def view_habits(self):
        c.execute("SELECT * FROM habits")
        records = c.fetchall()
        
        if records:
            top = tk.Toplevel()
            top.title("Your Habits")
            top.geometry("400x300")

            for index, record in enumerate(records):
                habit_label = tk.Label(top, text=f"{record[1]} - {record[2]}")
                habit_label.pack()

            close_btn = tk.Button(top, text="Close", command=top.destroy)
            close_btn.pack(pady=20)
        else:
            messagebox.showinfo("Info", "No habits tracked yet.")

# Running the application
if __name__ == '__main__':
    root = tk.Tk()
    app = HabitTracker(root)
    root.mainloop()

    conn.close()
