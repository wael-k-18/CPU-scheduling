
# 🎮 Preemptive CPU Scheduling (Shortest Remaining Time First - SRTF) 🎮

This project implements the **Shortest Remaining Time First (SRTF)** preemptive CPU scheduling algorithm with a user-friendly **GUI** built using Python's `tkinter` and `matplotlib`. The application allows users to input processes with arrival and burst times, display scheduling results in a table format, visualize the Gantt chart, and save/load process data.

## Features

- **Add Process**: Add processes with arrival and burst times.
- **Remove Process**: Remove selected processes.
- **Run SRTF Scheduling**: Run the Shortest Remaining Time First (SRTF) algorithm to calculate and display the waiting time, turnaround time, and completion time.
- **Gantt Chart**: Visualize the CPU scheduling with a Gantt chart showing each process' execution over time.
- **Process List**: View a list of all added processes.
- **Save and Load Processes**: Save the list of processes to a file and load it back later.
- **Error Handling**: Invalid inputs are handled gracefully with error messages.

## Installation

To run this project, you need to have Python installed on your machine. Additionally, install the following dependencies:

1. **tkinter**: Python GUI library (usually comes pre-installed with Python).
2. **matplotlib**: For generating the Gantt chart.

### Install dependencies

You can install the required libraries using `pip`:

```bash
pip install matplotlib
```

## How to Use

1. **Add Processes**: Enter the arrival time and burst time for a process and click on the "🔥 Add Process 🔥" button.
2. **Run SRTF Scheduling**: Click the "🎮 Run SRTF Scheduling 🎮" button to calculate the scheduling and display the results.
3. **Remove Process**: Select a process from the list and click on the "❌ Remove Process ❌" button to remove it.
4. **View Results**: The table below the input section will show the process details, including the waiting time, turnaround time, and completion time for each process.
5. **Gantt Chart**: A Gantt chart will be generated and displayed based on the scheduling results.
6. **Save and Load Processes**: Use the "💾 Save Processes 💾" and "📂 Load Processes 📂" buttons to save and load processes from a file.

## Screenshots

### Main UI

![Main UI Screenshot](./screenshots/main_ui.png)

### Gantt Chart

![Gantt Chart Screenshot](./screenshots/gantt_chart.png)

## File Structure

```
├── main.py                # Main application file
├── processes.txt          # Saved processes data file (optional)
├── screenshots/           # Folder containing screenshots of the UI
│   ├── main_ui.png
│   └── gantt_chart.png
└── README.md              # This readme file
```

## Example

1. **Add Processes**:
   - Arrival Time = 0, Burst Time = 6
   - Arrival Time = 1, Burst Time = 8
   - Arrival Time = 2, Burst Time = 7

2. **Run SRTF Scheduling**:
   - The program calculates waiting times, turnaround times, and completion times.
   - Displays the results in a table.
   - Generates a Gantt chart.

3. **Result Display**:
   ```
   Process | Arrival Time | Burst Time | Waiting Time | Turnaround Time | Completion Time
   ---------------------------------------------------------------------------
   P1      | 0            | 6          | 0            | 6               | 6
   P2      | 1            | 8          | 6            | 14              | 15
   P3      | 2            | 7          | 9            | 16              | 17
   ```

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, create a branch, and submit a pull request. Your contributions are welcome!

### Steps for Contribution

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to your branch (`git push origin feature-branch`).
6. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Python's `tkinter` for the GUI
- `matplotlib` for plotting the Gantt chart
- The concept of CPU scheduling algorithms from Operating System concepts
