# IP Address Sanitizer

This is a simple Python application with a graphical user interface (GUI) that reads a text file and sanitizes all IP addresses by replacing the dots (`.`) with `[.]`. This is useful for obfuscating IP addresses in text files when sharing them publicly.

## Features
- Reads a text file and identifies all valid IPv4 addresses.
- Sanitizes the IP addresses by replacing each `.` with `[.]`.
- Allows users to select both input and output files via a simple graphical interface.
- Saves the sanitized content to a new file.

## Prerequisites

- Python 3.x
- `tkinter` (This is usually pre-installed with Python, but if not, you can install it using your package manager.)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ip-address-sanitizer.git
    cd ip-address-sanitizer
    ```

2. (Optional) Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install any dependencies (if needed). The `tkinter` library should already be installed with Python by default, but you can ensure it's there:
    ```bash
    sudo apt-get install python3-tk  # For Debian/Ubuntu Linux
    ```

4. Run the script:
    ```bash
    python ip_sanitizer_gui.py
    ```

## Usage

1. Launch the application:
    ```bash
    python ip_sanitizer_gui.py
    ```

2. The GUI will open. Follow these steps:
    - **Select Input File**: Click the "Browse" button next to the **Input File** field and choose the `.txt` file that contains the IP addresses you want to sanitize.
    - **Select Output File**: Click the "Browse" button next to the **Output File** field and specify the location where the sanitized file should be saved.
    - **Sanitize IPs**: Once both file paths are entered, click the "Sanitize IPs" button to process the file. The sanitized IP addresses will be saved to the specified output file.

## Example

### Input:
If your input file contains the following content:
