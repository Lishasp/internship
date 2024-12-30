import tkinter as tk
from tkinter import messagebox

# Function to perform the selected operation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            result = num1 / num2

        label_result.config(text=f"Result: {result}")
    
    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid input! {str(e)}")

# Creating the main window
window = tk.Tk()
window.title("Basic Calculator")

# Creating and placing the UI components
label_num1 = tk.Label(window, text="Enter first number:")
label_num1.grid(row=0, column=0, padx=10, pady=5)

entry_num1 = tk.Entry(window)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(window, text="Enter second number:")
label_num2.grid(row=1, column=0, padx=10, pady=5)

entry_num2 = tk.Entry(window)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

# Dropdown menu for selecting operation
operation_var = tk.StringVar(window)
operation_var.set("Add")  # Default operation

operation_menu = tk.OptionMenu(window, operation_var, "Add", "Subtract", "Multiply", "Divide")
operation_menu.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Button to perform calculation
calc_button = tk.Button(window, text="Calculate", command=calculate)
calc_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Label to display result
label_result = tk.Label(window, text="Result:")
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the Tkinter event loop
window.mainloop()
