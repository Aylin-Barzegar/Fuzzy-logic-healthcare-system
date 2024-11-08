import tkinter as tk
from tkinter import messagebox
from validation import validate_inputs
from fuzzy_logic import run_fuzzy_logic
from plotting import show_membership_functions
from style import (
    BACKGROUND_COLOR,
    apply_entry_style,
    apply_status_label_style,
    apply_button_style,
    get_severity_color
)

def run_and_display():
    try:
        # Retrieve inputs and convert to floats
        temp_input = float(entry_temp.get())
        pulse_input = float(entry_pulse.get())
        spO2_input = float(entry_spo2.get())

        # Validate inputs
        if not validate_inputs(temp_input, pulse_input, spO2_input, entry_temp, entry_pulse, entry_spo2):
            return

        # Run fuzzy logic and capture the results
        severity_level, alert_message, alert_color = run_fuzzy_logic(temp_input, pulse_input, spO2_input)

        # If no severity level is calculated, show an error message
        if severity_level is None:
            messagebox.showerror("Calculation Error", alert_message)
            status_label.config(text="Severity Level\n Not calculated - No matching rule.", fg=alert_color)
            return

        # Update status label with severity level and message
        status_label.config(text=f"Severity Level: {severity_level:.2f}\n{alert_message}", fg=get_severity_color(severity_level))

        # Display membership function plots
        show_membership_functions(temp_input, pulse_input, spO2_input, severity_level)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numerical values for all inputs.")

# GUI setup remains the same
root = tk.Tk()
root.title("Health Monitoring System")
root.configure(bg=BACKGROUND_COLOR)

status_label = tk.Label(root, text="Severity Level \nNot calculated")
apply_status_label_style(status_label)
status_label.grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(root, text="Body Temperature (°C):", fg="white", bg=BACKGROUND_COLOR).grid(row=1, column=0, padx=10, pady=10)
entry_temp = tk.Entry(root)
apply_entry_style(entry_temp)
entry_temp.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Pulse Rate (BPM):", fg="white", bg=BACKGROUND_COLOR).grid(row=2, column=0, padx=10, pady=10)
entry_pulse = tk.Entry(root)
apply_entry_style(entry_pulse)
entry_pulse.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="SpO₂ Level (%):", fg="white", bg=BACKGROUND_COLOR).grid(row=3, column=0, padx=10, pady=10)
entry_spo2 = tk.Entry(root)
apply_entry_style(entry_spo2)
entry_spo2.grid(row=3, column=1, padx=10, pady=10)

evaluate_button = tk.Button(root, text="Evaluate Health Status", command=run_and_display)
apply_button_style(evaluate_button)
evaluate_button.grid(row=4, column=0, columnspan=2, pady=20)

root.mainloop()
