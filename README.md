SQL SA Password Reset Tool
Overview
This tool is a graphical user interface (GUI) developed in Python using the Tkinter library. It allows users to reset the SA (System Administrator) password for a specified SQL Server instance remotely. The tool utilizes PowerShell commands through subprocess calls to interact with the SQL Server services and the dbatools module.

Features
Reset SA Password: The tool resets the SA password for a specified SQL Server instance.

Instance Validation: Before attempting to reset the password, the tool checks if the provided SQL Server instance exists.

Asynchronous Operation: The password reset operation runs in a separate thread to prevent freezing the GUI during execution.

Prerequisites
Python 3.x
Tkinter library
PowerShell
Usage
Run the script using python script_name.py.

Fill in the required information:

Server: The name or IP address of the SQL Server.
Instance: The name of the SQL Server instance.
Username: The username for authentication.
New SA Password: The new SA password.
Click the "Reset SA Password" button.

Monitor the result label for the outcome of the password reset operation.

Author
Author: Walid Hocine
Role: System Engineer
GUI Components
Server: Entry widget for specifying the server name or IP address.

Instance: Entry widget for specifying the SQL Server instance name.

Username: Entry widget for providing the authentication username.

New SA Password: Entry widget for entering the new SA password.

Reset SA Password Button: Button for triggering the password reset operation.

Result Label: Displays the result of the password reset operation.

Author Label: Provides information about the author.

Notes
The tool uses the dbatools module, so it requires PowerShell to be available on the system.

Ensure that the provided SQL Server instance exists before attempting to reset the password.

For security reasons, it's recommended to run the tool on the machine where the SQL Server instance is hosted or in a secure network environment.
