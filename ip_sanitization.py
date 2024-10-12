import re
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to sanitize IP addresses
def sanitize_ip_addresses(input_file, output_file):
    ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

    try:
        # Open the input file and read its contents
        with open(input_file, 'r') as file:
            content = file.read()

        # Find all IP addresses and replace '.' with '[.]'
        sanitized_content = re.sub(ip_pattern, lambda x: x.group(0).replace('.', '[.]'), content)

        # Save the sanitized content to the output file
        with open(output_file, 'w') as file:
            file.write(sanitized_content)

        messagebox.showinfo("Success", f"Sanitized IP addresses saved to: {output_file}")

    except FileNotFoundError:
        messagebox.showerror("Error", f"File not found: {input_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to browse for input file
def browse_input_file():
    input_file = filedialog.askopenfilename(title="Select Input File", filetypes=[("Text Files", "*.txt")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, input_file)

# Function to browse for output file
def browse_output_file():
    output_file = filedialog.asksaveasfilename(title="Select Output File", defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_file)

# Function to execute the sanitization process
def run_sanitization():
    input_file = input_entry.get()
    output_file = output_entry.get()
    if input_file and output_file:
        sanitize_ip_addresses(input_file, output_file)
    else:
        messagebox.showwarning("Input Error", "Please provide both input and output file paths.")

# Create the GUI window
root = tk.Tk()
root.title("IP Address Sanitizer")

# Input file label and entry
input_label = tk.Label(root, text="Input File:")
input_label.grid(row=0, column=0, padx=10, pady=10)

input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1, padx=10, pady=10)

input_browse_btn = tk.Button(root, text="Browse", command=browse_input_file)
input_browse_btn.grid(row=0, column=2, padx=10, pady=10)

# Output file label and entry
output_label = tk.Label(root, text="Output File:")
output_label.grid(row=1, column=0, padx=10, pady=10)

output_entry = tk.Entry(root, width=50)
output_entry.grid(row=1, column=1, padx=10, pady=10)

output_browse_btn = tk.Button(root, text="Browse", command=browse_output_file)
output_browse_btn.grid(row=1, column=2, padx=10, pady=10)

# Run button
run_button = tk.Button(root, text="Sanitize IPs", command=run_sanitization)
run_button.grid(row=2, column=1, padx=10, pady=10)

# Start the GUI main loop
root.mainloop()
