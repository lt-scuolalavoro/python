import linecache

MAX_LINE = 194
date = []
count = -2
filename='flo_gen_output.txt'
for i in range(MAX_LINE):
    count = count + 12
    date.append(float(linecache.getline(filename, count).split()[-1]))
    
print("Minimum: " + str(min(date)))
print("Maximum: " + str(max(date)))
print("Average: " + "{0:.3f}".format(sum(date)/len(date)))