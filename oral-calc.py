import random

x = []{}
amount = 40

for i in range(0,amount):
    x[i]['x1'] = int(random.random()*100)*10
    x[i]['x2'] = int(random.random()*10)
    x[i]['result'] = x['x1']*x['x2']

for i in range(0, amount):
    print(x[i]['x1']," x ", x[i]['x2'], " = ")

for i in range(0, amount):
    print(x[i]['x1'], ' x ', x[i]['x2'], ' = ', x[i]['result'])

