import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")  # Set the size of the calculator window

# Entry widget to display calculations
display = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="solid")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Global variable to keep track of the expression
expression = ""

# Function to update the display when a button is clicked
def button_click(value):
    global expression
    expression += str(value)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)

# Function to evaluate the expression
def calculate():
    global expression
    try:
        result = eval(expression)  # Evaluate the expression
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))  # Display the result
        expression = str(result)  # Update the expression with the result
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""

# Function to clear the display
def clear_display():
    global expression
    expression = ""
    display.delete(0, tk.END)

# Define button values in a grid structure
button_texts = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Create buttons in the grid layout
for (text, row, col) in button_texts:
    if text == "=":
        btn = tk.Button(root, text=text, font=("Arial", 18), command=calculate)
    else:
        btn = tk.Button(root, text=text, font=("Arial", 18), command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Clear button
clear_btn = tk.Button(root, text="C", font=("Arial", 18), command=clear_display)
clear_btn.grid(row=0, column=3, sticky="nsew", padx=5, pady=5)

# Make rows and columns stretchable
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Run the application
root.mainloop()
