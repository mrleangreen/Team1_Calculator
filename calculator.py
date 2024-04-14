import tkinter as tk
from functools import partial

# This function updates the expression in the entry box when a button is pressed.
def calculate(operation):
    global expression
    # Clear the current expression if the 'AC' (All Clear) button is pressed.
    if operation == 'AC':
        expression = ''
    # If '=' is pressed, try to evaluate the current expression.
    elif operation == '=':
        try:
            # Evaluate the expression and convert the result to a string.
            expression = str(eval(expression))
        except Exception:
            # Display an error message if the expression is invalid.
            expression = "Error"
    # If '%' is pressed, convert the number to a percentage by dividing by 100
    elif operation == '%':
        try:
            # Append the division by 100 operation to the current expression
            expression = str(eval(expression + '/100'))
        except Exception:
            # Display an error message if the expression is invalid.
            expression = "Error"
    else:
        # Add the symbol or number of the button pressed to the expression.
        expression += str(operation)
    # Update the entry box with the current or new expression.
    result.set(expression)

# Initialize the main window for the calculator.
root = tk.Tk()
root.title("Calculator")
# Set the background color of the window to white.
root.configure(bg='white')

# This StringVar tracks the input/output shown in the calculator's display.
expression = ''
result = tk.StringVar()

# Create the display where calculations are shown, with a white background.
display = tk.Entry(root, textvariable=result, justify='right', font=('Arial', 20), bd=0, insertwidth=4, bg='white', fg='black')
# Place the display at the top, spanning across all button columns.
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=20, sticky='nsew')

# Define the styles for number and symbol buttons.
button_style = {
    'padx': 20, 'pady': 20, 'font': ('Arial', 18), 'relief': 'flat', 'bg': 'white', 'fg': 'black'
}
# Define the style for operator buttons to contrast the symbol buttons.
operator_button_style = {
    'padx': 20, 'pady': 20, 'font': ('Arial', 18), 'relief': 'flat', 'bg': 'black', 'fg': 'white'
}
# Define the style for symbol buttons for better visibility.
symbol_button_style = {
    'padx': 20, 'pady': 20, 'font': ('Arial', 18), 'relief': 'flat', 'bg': 'white', 'fg': 'black'
}

# The layout of the buttons, arranged by rows.
buttons = [
    ('(', ')', '%', 'AC'),
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

# Create the calculator buttons and place them on the grid.
for i, row in enumerate(buttons):
    for j, item in enumerate(row):
        # Bind the button press to the calculate function.
        action = partial(calculate, item)
        # Choose the button style based on its type (number, operator, or symbol).
        if item in {'/', '*', '-', '+', '='}:
            btn_style = symbol_button_style
        elif item in {'AC', '%', '(', ')'}:
            btn_style = button_style
        else:
            btn_style = button_style
        # Create and place the button in the grid.
        btn = tk.Button(root, text=item, command=action, **btn_style)
        # The '=' button spans two rows for a distinct appearance.
        if item == '=':
            btn.grid(row=i+1, column=j, rowspan=2, sticky='nsew')
        else:
            btn.grid(row=i+1, column=j, sticky='nsew')

# Ensure the buttons expand to fill the space when the window is resized.
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Start the main loop that waits for user input.
root.mainloop()