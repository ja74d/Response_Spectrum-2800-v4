import tkinter as tk

def submit():
    value1 = entry1.get()
    value2 = entry2.get()
    value3 = entry3.get()
    result_label.config(text=f"Input 1: {value1}\nInput 2: {value2}\nInput 3: {value3}")

# Create the main application window
app = tk.Tk()
app.title("Input Form")

# Create and place input fields and labels
label1 = tk.Label(app, text="Input 1:")
label1.pack()
entry1 = tk.Entry(app)
entry1.pack()

label2 = tk.Label(app, text="Input 2:")
label2.pack()
entry2 = tk.Entry(app)
entry2.pack()

label3 = tk.Label(app, text="Input 3:")
label3.pack()
entry3 = tk.Entry(app)
entry3.pack()

# Create and place a submit button
submit_button = tk.Button(app, text="Submit", command=submit)
submit_button.pack()

# Create and place a label to display the inputs
result_label = tk.Label(app, text="")
result_label.pack()

# Start the GUI application loop
app.mainloop()
