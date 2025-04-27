import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def srtf_scheduling(processes):
    n = len(processes)
    remaining_time = [p['burst_time'] for p in processes]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n
    time, completed = 0, 0
    min_remaining_time = float('inf')
    shortest, check = 0, False
    while completed != n:
        for i in range(n):
            if (processes[i]['arrival_time'] <= time and
                remaining_time[i] < min_remaining_time and
                remaining_time[i] > 0):
                min_remaining_time = remaining_time[i]
                shortest = i
                check = True
        if not check:
            time += 1
            continue
        remaining_time[shortest] -= 1
        min_remaining_time = remaining_time[shortest] if remaining_time[shortest] > 0 else float('inf')
        if remaining_time[shortest] == 0:
            completed += 1
            finish_time = time + 1
            completion_time[shortest] = finish_time
            waiting_time[shortest] = (finish_time - processes[shortest]['burst_time'] - processes[shortest]['arrival_time'])
            waiting_time[shortest] = max(0, waiting_time[shortest])
        time += 1
    for i in range(n):
        turnaround_time[i] = processes[i]['burst_time'] + waiting_time[i]
    return waiting_time, turnaround_time, completion_time

def validate_input(arrival, burst):
    try:
        arrival_time = int(arrival)
        burst_time = int(burst)
        if arrival_time < 0 or burst_time <= 0:
            raise ValueError
        return arrival_time, burst_time
    except ValueError:
        return None

def display_results(processes):
    waiting_time, turnaround_time, completion_time = srtf_scheduling(processes)
    avg_waiting_time = sum(waiting_time) / len(processes)
    avg_turnaround_time = sum(turnaround_time) / len(processes)
    result_area.delete(*result_area.get_children())  # Clear table before updating
    for i, p in enumerate(processes):
        result_area.insert('', 'end', values=(f"P{i+1}", p['arrival_time'], p['burst_time'],
                                             waiting_time[i], turnaround_time[i], completion_time[i]))
    avg_label.config(text=f"Average Waiting Time: {avg_waiting_time:.2f}\n"
                          f"Average Turnaround Time: {avg_turnaround_time:.2f}")
    draw_gantt_chart(processes, completion_time)

def draw_gantt_chart(processes, completion_time):
    global canvas  # Use the global canvas variable

    # Check if canvas exists, and if it does, destroy the previous chart
    if 'canvas' in globals():
        canvas.get_tk_widget().destroy()  # Remove the previous chart

    fig, ax = plt.subplots(figsize=(8, 2))
    ax.set_title("Gantt Chart")
    ax.set_xlabel("Time")
    ax.set_yticks([])

    colors = ['#FF6347', '#4682B4', '#3CB371', '#FFD700', '#8A2BE2']  # Example colors
    start = 0
    for i, p in enumerate(processes):
        ax.barh(0, p['burst_time'], left=start, height=0.5, color=colors[i % len(colors)])
        ax.text(start + p['burst_time'] / 2, 0, f"P{i+1} (T={completion_time[i]})", ha='center', va='center', color='white', fontsize=10)
        start += p['burst_time']

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().place(x=300, y=500, width=900, height=200)
    canvas.draw()

def add_process():
    arrival_time = arrival_entry.get()
    burst_time = burst_entry.get()
    valid_input = validate_input(arrival_time, burst_time)
    if valid_input:
        arrival_time, burst_time = valid_input
        processes.append({'arrival_time': arrival_time, 'burst_time': burst_time})
        process_list.insert(tk.END, f"🚀 Process P{len(processes)}: Arrival Time={arrival_time}, Burst Time={burst_time}")
        arrival_entry.delete(0, tk.END)
        burst_entry.delete(0, tk.END)
        processes.sort(key=lambda p: p['arrival_time'])  # Sort processes by arrival time
    else:
        error_label.config(text="❌ Invalid input! Please enter non-negative integers. ❌")

def remove_process():
    selected_index = process_list.curselection()
    if selected_index:
        process_list.delete(selected_index)
        del processes[selected_index[0]]

def clear_all():
    processes.clear()
    process_list.delete(0, tk.END)
    result_area.delete(*result_area.get_children())
    avg_label.config(text="")
    error_label.config(text="")
    
    # Remove Gantt chart if it exists
    if 'canvas' in globals():
        canvas.get_tk_widget().destroy()

def show_process_details(event):
    selected_item = result_area.selection()[0]
    process_info = result_area.item(selected_item, "values")
    process_details_label.config(text=f"🎮 Process Details: {process_info} 🎮")

def save_processes_to_file():
    with open("processes.txt", "w") as f:
        for p in processes:
            f.write(f"{p['arrival_time']} {p['burst_time']}\n")

def load_processes_from_file():
    with open("processes.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            arrival, burst = map(int, line.strip().split())
            processes.append({'arrival_time': arrival, 'burst_time': burst})
            process_list.insert(tk.END, f"🚀 Process P{len(processes)}: Arrival Time={arrival}, Burst Time={burst}")

root = tk.Tk()
root.title("🎮 Preemptive CPU Scheduling (SRTF) 🎮")
root.geometry("800x600")
root.config(bg="#2c2c2c")  # Dark background

# Title label with fun font and emoji
title_label = tk.Label(root, text="🎮 Preemptive CPU Scheduling (Shortest Remaining Time First) 🎮", fg="white",
                       bg="#2c2c2c", font=("Comic Sans MS", 18, "bold"))
title_label.pack(pady=10)

# Input Frame
input_frame = tk.Frame(root, bg="#2c2c2c")
input_frame.pack(pady=10)

# Arrival and Burst Time labels
tk.Label(input_frame, text="🚀 Arrival Time:", fg="white", bg="#2c2c2c", font=("Comic Sans MS", 12)).grid(row=0, column=0, padx=5)
arrival_entry = tk.Entry(input_frame, width=10, font=("Comic Sans MS", 12))
arrival_entry.grid(row=0, column=1, padx=5)

tk.Label(input_frame, text="⚡ Burst Time:", fg="white", bg="#2c2c2c", font=("Comic Sans MS", 12)).grid(row=0, column=2, padx=5)
burst_entry = tk.Entry(input_frame, width=10, font=("Comic Sans MS", 12))
burst_entry.grid(row=0, column=3, padx=5)

# Add Process button with emoji
add_button = tk.Button(input_frame, text="🔥 Add Process 🔥", command=add_process, bg="#5a2d82", fg="white", font=("Comic Sans MS", 12))
add_button.grid(row=0, column=4, padx=10)

# Error label for invalid inputs
error_label = tk.Label(root, text="", fg="red", bg="#2c2c2c", font=("Comic Sans MS", 10))
error_label.pack(pady=5)

# Process list (listbox with a fun design)
processes = []

process_list = tk.Listbox(root, width=80, height=5, bg="#333", fg="white", font=("Comic Sans MS", 12))
process_list.pack(pady=5)

# Table for results with emojis
cols = ("🎮 Process", "⏰ Arrival Time", "⚡ Burst Time", "⏳ Waiting Time", "🕹 Turnaround Time", "💥 Completion Time")
result_area = ttk.Treeview(root, columns=cols, show="headings")
for col in cols:
    result_area.heading(col, text=col)
result_area.pack(pady=10)

# Average time labels with emojis
avg_label = tk.Label(root, text="", fg="white", bg="#2c2c2c", font=("Comic Sans MS", 12))
avg_label.pack(pady=10)

# Process details label with emojis
process_details_label = tk.Label(root, text="", fg="white", bg="#2c2c2c", font=("Comic Sans MS", 12))
process_details_label.pack(pady=10)

# Run, Clear, Remove, Save, and Load buttons with emojis
run_button = tk.Button(root, text="🎮 Run SRTF Scheduling 🎮", command=lambda: display_results(processes), bg="#5a2d82", fg="white", font=("Comic Sans MS", 12, "bold"))
run_button.pack(pady=10)

clear_button = tk.Button(root, text="🧹 Clear All 🧹", command=clear_all, bg="#FF6347", fg="white", font=("Comic Sans MS", 12))
clear_button.pack(pady=5)

remove_button = tk.Button(root, text="❌ Remove Process ❌", command=remove_process, bg="#FF6347", fg="white", font=("Comic Sans MS", 12))
remove_button.pack(pady=5)

save_button = tk.Button(root, text="💾 Save Processes 💾", command=save_processes_to_file, bg="#5a2d82", fg="white", font=("Comic Sans MS", 12))
save_button.pack(pady=5)

load_button = tk.Button(root, text="📂 Load Processes 📂", command=load_processes_from_file, bg="#5a2d82", fg="white", font=("Comic Sans MS", 12))
load_button.pack(pady=5)

result_area.bind("<ButtonRelease-1>", show_process_details)

root.mainloop()