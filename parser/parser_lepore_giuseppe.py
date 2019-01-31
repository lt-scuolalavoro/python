import linecache

filename = 'flo_gen_output.txt'
imgs = 194
data = []
linesperimg = 12
i = 10
while i < imgs * linesperimg:
    line = linecache.getline(filename, i)
    data.append(float(line.split()[-1]))
    i += linesperimg

nValues = len(data)
maxValue = max(data)
minValue = min(data)
avgValue = sum(data)/len(data)

print("Values parsed: %s" % nValues)
print("Min value: %s" % minValue)
print("Max value: %s" % maxValue)
print("Average value: %.8s" % avgValue)
