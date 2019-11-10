import random
import pandas as pd

x = []
amount = 40
param1 = "参数1"
param2 = "参数2"
result = "结果"

for i in range(0,amount):
    y = {}
    y[param1] = int(random.random()*100)*10
    y[param2] = int(random.random()*10)
    y[result] = y[param1] * y[param2]
    x.append(y)

for i in range(0, amount):
    print(x[i][param1]," x ", x[i][param2], " = ")

for i in range(0, amount):
    print(x[i][param1], ' x ', x[i][param2], ' = ', x[i][result])

df1 = pd.DataFrame(x)
print(df1)

export_file_name = r"./exported.xlsx"

# df1.to_excel(excel_writer=r"./exported.xlsx", sheet_name="Qi Qi's calculations")
# df1.to_excel(excel_writer=r"./exported.xlsx", sheet_name="Qi Qi's calculations", index=False)
# df1.to_excel(excel_writer=r"./exported.xlsx", sheet_name="Qi Qi's calculations", index=False, columns=["x1", "x2"])
df1.to_excel(excel_writer=export_file_name, 
    sheet_name="Qi Qi's calculations", 
    index=False, 
    columns=[param1, param2, result],
    encoding="utf-8")

