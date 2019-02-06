import linecache
def parser(filename, nImgs, linesDifference):
	f = open(filename, "r")
	data = []
	i=10
	while i<nImgs*12:
		data.append(float(linecache.getline(filename, i).split()[-1]))
		i+=linesDifference
	return data

data=parser("flo_gen_output.txt", 194, 12)
print("Values scanned: %d" % len(data))
print("Maximum value: %s" % max(data))
print("Minimum value: %s" % min(data))
print("Average value: %.3f" % (sum(data)/len(data)))