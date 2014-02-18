from hashlib import md5

data = {}

with open('wordlist.txt', 'r') as file:
    for line in file:
        line = line.strip()
        sorted = list(line)
        sorted.sort()
        sorted_str = ''.join(sorted)
        #useless it'd be enough to use the sorted lines as keyset
        data[md5(sorted_str).digest()] = line

solution = []

with open('process.txt', 'r') as file:
    for line in file:
        line = line.strip()
        sorted = list(line)
        sorted.sort()
        sorted_str = ''.join(sorted)
        solution.extend( [data[md5(sorted_str).digest()]] )

string = ''
        
for x in solution:
    string += x
    string += ','

string = string[0:len(string)-1]

print(string)
