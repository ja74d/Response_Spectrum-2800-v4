import tkinter as tk
from tkinter import ttk
import time
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

selected_value1 = None
selected_value2 = None
selected_value3 = None

def submit():
    global selected_value1, selected_value2, selected_value3
    selected_value1 = combobox1.get()
    selected_value2 = entry2.get()
    selected_value3 = combobox.get()
    app.after(2000, app.destroy())
    #app.destroy()
    #result_label.config(text=f"Input 1: {value1}\nInput 2: {value2}\nInput 3: {value3}")

# Create the main application window
app = tk.Tk()
app.title("Input Form")

# Create and place input fields and labels using a grid layout
label1 = tk.Label(app, text="Soil Type:")
label1.grid(row=0, column=0, padx=10, pady=5, sticky="w")
dropdown_options = ["I", "II", "III", "IV"]
combobox1 = ttk.Combobox(app, values=dropdown_options, state="readonly", width=20)
combobox1.grid(row=0, column=1, padx=10, pady=5)

label2 = tk.Label(app, text="A:")
label2.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry2 = tk.Entry(app)
entry2.grid(row=1, column=1, padx=10, pady=5)

label3 = tk.Label(app, text="Relative risk:")
label3.grid(row=2, column=0, padx=10, pady=5, sticky="w")

# Create a list of options for the dropdown
dropdown_options = ["Low", "Average", "Much", "Too Much"]

# Create and place the dropdown
combobox = ttk.Combobox(app, values=dropdown_options, state="readonly", width=20)
combobox.grid(row=2, column=1, padx=10, pady=5)

# Create and place a submit button
submit_button = tk.Button(app, text="Submit", command=submit)
submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create and place a label to display the inputs
result_label = tk.Label(app, text="", justify="left")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="w")

# Configure grid column weights to make input fields expandable
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)


# Start the GUI application loop
app.mainloop()

#the game begins here!

soil = selected_value1
A = selected_value2

if selected_value3 == "Low" or selected_value3 == "Average":

    if soil == "III":
        T0 = 0.15
        Ts = 0.7
        S = 1.75
        S0 = 1.1
    elif soil == "I":
        T0 = 0.1
        Ts = 0.4
        S = 1.5
        S0 = 1
    elif soil == "II":
        T0 = 0.1
        Ts = 0.5
        S = 1.5
        S0 = 1
    elif soil == "IV":
        T0 = 0.15
        Ts = 1
        S = 2.25
        S0 = 1.3

else:
    if soil == "III":
        T0 = 0.15
        Ts = 0.7
        S = 1.75
        S0 = 1.1
    elif soil == "I":
        T0 = 0.1
        Ts = 0.4
        S = 1.5
        S0 = 1
    elif soil == "II":
        T0 = 0.1
        Ts = 0.5
        S = 1.5
        S0 = 1
    elif soil == "IV":
        T0 = 0.15
        Ts = 1
        S = 1.75
        S0 = 1.1



T = []
B1 = []
N = []
B = []

for i in np.arange(0, 4.6, 0.001):
    #i = str(i)
    #i = i[0:5]
    #i = float(i)
    T.append(i)

print(len(T))
#print(T)

for x in T:
    if x >= 0 and x < T0:
        b1 = S0 + (S-S0+1)*(x/T0)
        B1.append(b1)
    elif x >= T0 and x <Ts:
        b1 = S+1
        B1.append(b1)
    elif x >= Ts:
        b1 = (S+1)*(Ts/x)
        B1.append(b1)
print(len(B1))
#print(B1)

for y in T:
    if y < Ts:
        n = 1
        N.append(n)

    elif y >= Ts and y < 4:
        n = ((0.7*y - 0.7*Ts)/(4-Ts))+1
        N.append(n)

    elif y >= 4:
        n = 1.7
        N.append(n)

print(len(N))

Ypoint = np.array(B1)
Xpoint = np.array(T)
#point = np.array(N)



plt.plot(Xpoint, Ypoint)

plt.xlim([0, max(Xpoint)+0.5])
plt.ylim([0, max(Ypoint)+0.5])


plt.title(f'Response Spectrum For Soil{soil}')
plt.xlabel("T(Sec)")
plt.ylabel("B1")

#Pic Saving
plt.savefig('plot image.png')

image_path = "/home/javad/Response_Spectrum-2800-v4/plot image.png"

#Excel Output
Data = {"T":Xpoint, "B1":Ypoint, "N":np.array(N, dtype=object)}
df = pd.DataFrame(Data)

df['B'] = df.B1 * df.N

df.to_excel("output.xlsx", index=False)

writer = pd.ExcelWriter("output.xlsx", engine="xlsxwriter")
df.to_excel(writer, sheet_name="Sheet1", index=False)
worksheet = writer.sheets["Sheet1"]

# Insert the image into the Excel file
worksheet.insert_image("E2", image_path)  # Adjust the cell reference as needed

# Save the Excel file using the Pandas ExcelWriter object
writer.close()

plt.show()




