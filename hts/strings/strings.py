

primes_dict = [2,3,5,7]

fd = open('data.txt', 'r')
string = fd.read()
string = string.strip()
primes = []
comps = []
alpha = []

for c in string:
    try:
        num = int(c)
        if num != 0 and num != 1:
            if num in primes_dict:
                primes.extend([num])
            else:
                comps.extend([num])
    except ValueError:
        if len(alpha) < 25:
            alpha.extend([c])

numerics = sum(primes)*sum(comps)
alpha = [ chr(ord(x)+1) for x in alpha ]
print( ''.join(alpha)+str(numerics) )
