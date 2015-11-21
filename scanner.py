import urllib

def baseN(num, b, numerals="01"):
	return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

maxi = 127
mini = 0
length = 7

server = "http://eastinitiative.org/"
ndork = "404"
fill = "0"

for a in range(mini, maxi):
    num = baseN(a, 2)
    num0 = fill*(length-len(num)) + num
    data = urllib.urlopen(server + num0).read()
    if ndork not in data:
        print(server + num0)

# Over complicating things can be fun sometimes :D
