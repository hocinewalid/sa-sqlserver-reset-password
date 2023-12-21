# SQL SA Password Reset Tool

## Overview

This tool provides a user-friendly GUI to reset the SA (System Administrator) password for a specified SQL Server instance remotely. Developed in Python using the Tkinter library, the tool seamlessly interacts with SQL Server services using PowerShell commands and the dbatools module.

## Features

- **Reset SA Password:** Easily reset the SA password for a designated SQL Server instance.
- **Instance Validation:** Verify the existence of the specified SQL Server instance before attempting password reset.
- **Asynchronous Operation:** Execute password reset in a separate thread to ensure a responsive GUI.

## Prerequisites

- Python 3.x
- Tkinter library
- PowerShell

## Usage

1. Run the script using `python script_name.py`.
2. Fill in the required information:
   - **Server:** The SQL Server's name or IP address.
   - **Instance:** The name of the SQL Server instance.
   - **Username:** Authentication username.
   - **New SA Password:** Desired new SA password.
3. Click the "Reset SA Password" button.
4. Monitor the result label for the outcome of the password reset operation.

## Author

- **Author:** Walid Hocine
- **Role:** System Engineer

## GUI Components

- **Server:** Entry widget for specifying the server name or IP address.
- **Instance:** Entry widget for specifying the SQL Server instance name.
- **Username:** Entry widget for providing the authentication username.
- **New SA Password:** Entry widget for entering the new SA password.
- **Reset SA Password Button:** Button for triggering the password reset operation.
- **Result Label:** Displays the result of the password reset operation.
- **Author Label:** Provides information about the author.

## Notes

- The tool uses the dbatools module, requiring PowerShell to be available.
- Ensure the specified SQL Server instance exists before attempting password reset.
- For security reasons, run the tool on the machine hosting the SQL Server instance or in a secure network environment.

## License

This tool is provided under the [MIT License](LICENSE).
