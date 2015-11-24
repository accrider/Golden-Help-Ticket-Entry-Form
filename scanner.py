import urllib

server = "http://eastinitiative.org/"

for a in range(0, 2**7):
	num = "{0:b}".format(a)
	num = ("0"*(7 - len(num))) + num
	data = urllib.urlopen(server + num).read()
	
	print("Trying: " + server + num)
	if "404" not in data:
		print("Solution: " + server + num)
		break