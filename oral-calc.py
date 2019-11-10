import random

x = []
amount = 40

for i in range(0,amount):
    y = {}
    y['x1'] = int(random.random()*100)*10
    y['x2'] = int(random.random()*10)
    y['result'] = y['x1'] * y['x2']
    x.append(y)

for i in range(0, amount):
    print(x[i]['x1']," x ", x[i]['x2'], " = ")

for i in range(0, amount):
    print(x[i]['x1'], ' x ', x[i]['x2'], ' = ', x[i]['result'])

