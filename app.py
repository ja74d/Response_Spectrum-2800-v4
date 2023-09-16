import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

#A=0.25

soil = input(str("your soil name:"))

A = 0.25

if soil == "3":
    T0 = 0.15
    Ts = 0.7
    S = 1.75
    S0 = 1.1
elif soil == "1":
    T0 = 0.1
    Ts = 0.4
    S = 1.5
    S0 = 1
elif soil == "2":
    T0 = 0.1
    Ts = 0.5
    S = 1.5
    S0 = 1
elif soil == "4":
    T0 = 0.15
    Ts = 1
    S = 2.25
    S0 = 1.3




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
Data = {"T":Ypoint, "B1":Xpoint, "N":np.array(N, dtype=object)}
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



