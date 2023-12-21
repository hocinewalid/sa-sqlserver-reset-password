import tkinter as tk
from tkinter import messagebox
import threading
import subprocess
import getpass

# Author: Walid Hocine, System Engineer

def is_instance_exists(server, instance):
    try:
        # Use subprocess to call PowerShell with Get-Service command
        command = f"powershell -Command \"Get-Service -ComputerName {server} -Name '{instance}'\""
        result = subprocess.run(command, check=False, capture_output=True, text=True, shell=True, timeout=5)

        # Check if the command was successful (return code 0) and if the service is found
        return result.returncode == 0 and instance in result.stdout

    except subprocess.TimeoutExpired:
        # Timeout expired, instance check took too long
        return False
    except Exception as e:
        # Other errors
        return False

def reset_sa_password(server, instance, username, new_password, result_var):
    try:
        if not server or not instance or not username or not new_password:
            raise ValueError("All fields must be filled.")

        # Check if the SQL Server instance exists
        if not is_instance_exists(server, instance):
            messagebox.showerror("Error", f"SQL Server instance '{instance}' does not exist.")
            return

        # Use subprocess to call PowerShell with dbatools command
        command = f"powershell -Command \"Import-Module dbatools; $securePassword = ConvertTo-SecureString -String {new_password} -AsPlainText -Force; $cred = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList ('{username}', $securePassword); Reset-DbaAdmin -SqlInstance {server}\\{instance} -SqlCredential $cred -Confirm:$false\""
        result = subprocess.run(command, capture_output=True, text=True, shell=True)

        if result.returncode == 0:
            result_var.set("SA password reset successfully.")
        else:
            messagebox.showerror("Error", result.stderr.strip())
            result_var.set("Error resetting SA password.")

    except Exception as e:
        messagebox.showerror("Error", str(e))
        result_var.set("Error resetting SA password.")

def reset_password_button_clicked():
    server = entry_server.get()
    instance = entry_instance.get()  # New field for SQL Server instance
    username = entry_username.get()
    new_password = entry_new_password.get()

    # Validate input fields
    if not server or not instance or not username or not new_password:
        messagebox.showwarning("Warning", "All fields must be filled.")
        return

    # If the script is not run interactively, prompt for the new password
    if new_password == "":
        new_password = getpass.getpass("Enter the new SA password: ")

    # Create a Tkinter variable to store the result message
    result_var = tk.StringVar()

    # Create a separate thread to run the reset_sa_password function
    reset_thread = threading.Thread(target=reset_sa_password, args=(server, instance, username, new_password, result_var))
    reset_thread.start()

    # Check the status of the thread periodically
    window.after(100, check_thread_status, reset_thread, result_var)

def check_thread_status(thread, result_var):
    if not thread.is_alive():
        # Thread has finished, update the result label
        result_label.config(text=result_var.get(), fg="green" if "successfully" in result_var.get() else "red")
    else:
        # Thread is still running, check again after 100 milliseconds
        window.after(100, check_thread_status, thread, result_var)

# GUI setup
window = tk.Tk()
window.title("SQL SA Password Reset Tool - Authored by Walid Hocine")

# Reduce the window size by 15%
window_width = int(600 * 0.85)
window_height = int(400 * 0.85)

# Set the window size and make it non-resizable
window.geometry(f"{window_width}x{window_height}")
window.resizable(False, False)

# Font settings
font = ("Arial", 12)  # Change font to Arial and increase size

# Labels
label_server = tk.Label(window, text="Server:", font=font)
label_instance = tk.Label(window, text="Instance:", font=font)  # New label for SQL Server instance
label_username = tk.Label(window, text="Username:", font=font)
label_new_password = tk.Label(window, text="New SA Password:", font=font)
label_author = tk.Label(window, text="Tool authored by Walid Hocine", font=("Arial", 10), fg="gray")

# Entry widgets
entry_server = tk.Entry(window, width=30, font=font)
entry_instance = tk.Entry(window, width=30, font=font)  # New entry for SQL Server instance
entry_username = tk.Entry(window, width=30, font=font)
entry_new_password = tk.Entry(window, show="*", width=30, font=font)

# Button
reset_button = tk.Button(window, text="Reset SA Password", command=reset_password_button_clicked, font=font)

# Result label
result_label = tk.Label(window, text="", fg="black", font=font)

# Center the widgets
center_frame = tk.Frame(window)
center_frame.grid(row=0, column=0, padx=50, pady=50)

label_server.grid(row=0, column=0, sticky=tk.E, pady=(5, 5))
label_instance.grid(row=1, column=0, sticky=tk.E, pady=(5, 5))  # New position for SQL Server instance
label_username.grid(row=2, column=0, sticky=tk.E, pady=(5, 5))
label_new_password.grid(row=3, column=0, sticky=tk.E, pady=(5, 5))

entry_server.grid(row=0, column=1)
entry_instance.grid(row=1, column=1)  # New position for SQL Server instance
entry_username.grid(row=2, column=1)
entry_new_password.grid(row=3, column=1)

reset_button.grid(row=4, column=1, pady=10)
result_label.grid(row=5, column=1)

label_author.grid(row=6, column=1, pady=(0, 10))  # Adjust row number as needed

# Run the GUI
window.mainloop()
