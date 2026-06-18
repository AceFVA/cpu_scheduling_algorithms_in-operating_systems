# Operating Systems: CPU Scheduling Algorithms

# In this program, we will implement various CPU scheduling algorithms in Python. The algorithms we will cover include:
# 1. First-Come, First-Served (FCFS)
# 2. Shortest Job Next (SJN) (Preemptive and Non-Preemptive)
# 3. Priority Scheduling (Preemptive and Non-Preemptive)
# 4. Round Robin (RR)

# This program will allow users to input the number of processes, their burst times, arrival times, and priorities (if applicable).
# This will then calculate and display the average turnararound time and average waiting time for the selected scheduling algorithm 
# with the use of Tkinter for visualization of the Gantt chart as well.

import tkinter as tk
from tkinter import messagebox

class CPUScheduling:
    def __init__(self, root):
        # Application window layout and configuration
        self.root = root
        self.root.title("CPU Scheduling Algorithms")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f"{screen_width}x{screen_height}")
        root.state("zoomed")

if __name__ == "__main__":
    root =tk.Tk()
    app = CPUScheduling(root)
    root.mainloop()