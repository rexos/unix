from string import letters

data = []
processed = []
final = [0]
with open('cipher.txt', 'r') as file:
    for line in file:
        line = line.strip()
        line = line.strip('.')
        line = line.split('.')
        data.extend([int(x) for x in line])

start = data[0] + data[1] + data[2]

for i in range(5,len(data), 3):
    sum = data[i] + data[i-1] + data[i-2]
    final.extend([sum - start])


for key in range(73, 256 - 38):
    tmp = [ chr(x + key) for x in final ]
    print(''.join(tmp))

