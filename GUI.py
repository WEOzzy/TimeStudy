import tkinter as tk
from tkinter import messagebox

# create the main tkinter app window
app = tk.Tk()
app.title="Time Study"
app.geometry("720x250")

#list to store user inputs
user_inputs = []

# add dynamically generated input fields
def add_input_fields(num_fields):
    for i in range(num_fields):
        # label each input
        tk.Label(app, text=f"Input {i + 1}").pack()
        # create an entry widget for user input and store it in the list
        entry = tk.Entry(app)
        entry.pack()
        user_inputs.append(entry) # store the entry widget in the list

# entry widget for the user to input the number of fields
num_fields_entry = tk.Entry(app)
num_fields_entry.pack()

# function to retrieve user input, add the input fields, and add a button to print values
def get_num_fields():
    try:
        num_fields = int(num_fields_entry.get())
        add_input_fields(num_fields)
    except ValueError:
        # display an error, shouldn't be necessary once I repurpose
        tk.messagebox.showerror("Error", "Please enter a number.")

    # add a button to trigger printing the values
    print_values_button = tk.Button(app, text="Print Values", command=print_values)
    print_values_button.pack()

# function to print user inputs on the console
def print_values():
    values = [entry.get() for entry in user_inputs]
    print("User inputs:", values)

# button to trigger the addition of input fields
add_fields_button = tk.Button(app, text="Add Input Fields", command=get_num_fields)
add_fields_button.pack()

# run the main loop to show the gui and handle interactions
app.mainloop()

# it would be absolutely hideous but I could append most of what I have here and map it to the gui...